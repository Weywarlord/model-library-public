"""Download a versioned model package. Does not execute it or access credentials."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile
import urllib.parse
import urllib.request
import zipfile

MAX_BYTES = 32 * 1024 * 1024
ID = re.compile(r'[a-z0-9][a-z0-9._-]{0,79}\Z')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise ValueError('REDIRECT_NOT_ALLOWED')


def relative_path(value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('INVALID_RELATIVE_PATH')
    parts = value.split('/')
    if any(p in ('', '.', '..') or ':' in p for p in parts):
        raise ValueError('INVALID_RELATIVE_PATH')
    return PurePosixPath(value)


def fetch(url, origin, local=False, limit=MAX_BYTES):
    p, o = urllib.parse.urlsplit(url), urllib.parse.urlsplit(origin)
    allowed = p.scheme == 'https' or (local and p.scheme == 'http' and p.hostname == '127.0.0.1')
    if not allowed or (p.scheme, p.netloc) != (o.scheme, o.netloc) or p.username or p.password or p.query or p.fragment:
        raise ValueError('HTTPS_SAME_ORIGIN_URL_REQUIRED')
    request = urllib.request.Request(url, headers={'User-Agent': 'model-library/1.0'})
    with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as response:
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError('DOWNLOAD_TOO_LARGE')
    return data


def unpack(data, target):
    """Validate entire ZIP before creating any installed file."""
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = archive.infolist()
        if len(infos) > 200 or sum(i.file_size for i in infos) > MAX_BYTES:
            raise ValueError('ARCHIVE_TOO_LARGE')
        if len({i.filename for i in infos}) != len(infos):
            raise ValueError('DUPLICATE_ARCHIVE_PATH')
        for item in infos:
            path = relative_path(item.filename)
            mode = item.external_attr >> 16
            if item.is_dir() or stat.S_ISLNK(mode) or stat.S_IFMT(mode) not in (0, stat.S_IFREG):
                raise ValueError('ARCHIVE_FILE_TYPE_REJECTED')
            if set(p.lower() for p in path.parts) & {'private', 'secret', '.git', '.env', '.dev.vars'}:
                raise ValueError('PRIVATE_PATH_REJECTED')
        manifest = json.loads(archive.read('MANIFEST.sha256.json'))
        if set(manifest) != {i.filename for i in infos} - {'MANIFEST.sha256.json'}:
            raise ValueError('ARCHIVE_MANIFEST_MISMATCH')
        for name, digest in manifest.items():
            if hashlib.sha256(archive.read(name)).hexdigest() != digest:
                raise ValueError('ARCHIVE_FILE_HASH_MISMATCH')
        for item in infos:
            destination = target.joinpath(*PurePosixPath(item.filename).parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(archive.read(item.filename))


def install(catalog_url, model, directory, local=False):
    if not ID.fullmatch(model):
        raise ValueError('MODEL_ID_INVALID')
    catalog = json.loads(fetch(catalog_url, catalog_url, local, 1024 * 1024))
    if catalog.get('catalog_version') != 1:
        raise ValueError('CATALOG_VERSION_UNSUPPORTED')
    entries = [m for m in catalog['models'] if m['id'] == model]
    if len(entries) != 1:
        raise ValueError('MODEL_NOT_FOUND_OR_DUPLICATED')
    manifest_url = urllib.parse.urljoin(catalog_url, str(relative_path(entries[0]['manifest'])))
    manifest = json.loads(fetch(manifest_url, catalog_url, local, 1024 * 1024))
    release = manifest['release']
    if manifest.get('manifest_version') != 1 or manifest['model_id'] != model or not ID.fullmatch(release):
        raise ValueError('MODEL_MANIFEST_MISMATCH')
    package_url = urllib.parse.urljoin(manifest_url, str(relative_path(manifest['package']['path'])))
    target = Path(directory).absolute() / model / release
    directory = Path(directory).absolute()
    if directory.is_symlink() or any(p.is_symlink() for p in (target, target.parent)):
        raise ValueError('SYMLINK_TARGET_REJECTED')
    if target.exists():
        raise ValueError('VERSION_ALREADY_INSTALLED_USE_EXISTING_DIRECTORY')
    data = fetch(package_url, catalog_url, local)
    if hashlib.sha256(data).hexdigest() != manifest['package']['sha256']:
        raise ValueError('PACKAGE_HASH_MISMATCH')
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.model-download-', dir=target.parent) as temporary:
        stage = Path(temporary) / 'package'
        stage.mkdir()
        unpack(data, stage)
        for key in ('prompt', 'skill', 'instructions'):
            item = manifest[key]
            path = stage.joinpath(*relative_path(item['installed_path']).parts)
            if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
                raise ValueError('MODEL_CONTENT_HASH_MISMATCH')
        (stage / 'MODEL-RECEIPT.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
        # Atomic directory rename; an existing populated installation cannot be replaced.
        if target.exists():
            raise ValueError('VERSION_ALREADY_INSTALLED_USE_EXISTING_DIRECTORY')
        stage.rename(target)
    return {'status': 'installed', 'directory': str(target),
            'read_first': str(target / manifest['instructions']['installed_path']),
            'activated': False, 'compute_called': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--allow-local-http', action='store_true', help='127.0.0.1 acceptance tests only')
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.catalog, args.model, args.directory, args.allow_local_http), ensure_ascii=False))
    except Exception as exc:
        # Do not echo URLs, local files or arbitrary remote error bodies.
        print(json.dumps({'status':'error', 'code':str(exc) if isinstance(exc, ValueError) else type(exc).__name__}))
        raise SystemExit(1)
