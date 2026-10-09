# Relationship Insight — Risk Analysis

Organize observations. Verify details. Explore the model's assessment.

Install and activate once. Then describe what you have observed to your local AI. It will prepare a fact-check card and wait for your confirmation before requesting a computation.

## Before you begin

You need a local AI client that can read HTTPS files, save local files and run Python 3.12 or newer. macOS has been tested; Linux has not been tested on a physical device, and Windows is not supported in this release. A chat-only app cannot install or run this product. No MCP connector, browser extension or always-running background service is required.

Keep these two items from your order:

- Your unique **License key**. `Product Key: pFVqj` is the product ID, not an activation code.
- Your public startup link, provided in the order's Start Here attachment.

Keep the full extracted package, including the hidden `.agents` directory. The API address is already configured; do not replace it with an old service address.

## 1. Ask your AI to prepare the installation

> Read this guide and `.agents/skills/relationship-evaluator/SKILL.md` in this project. Check that the Python executable you will actually use is 3.12 or newer. Explain what you will download, install and run, and request the necessary file and network permissions. Use a project-local environment. Do not run a computation yet.

Clients without a Skill feature can read those files directly. If the default `python3` is too old, use the actual path of an installed Python 3.12+ executable. If none is available, explain how to obtain it from the official Python source and get installation authorization first. Do not replace macOS system Python.

For the AI, from the installed `workers-compute` directory:

```sh
cd "/absolute/path/to/the/installed/workers-compute"
python3 -m venv .venv
.venv/bin/python -m pip install -r customer_release/requirements.txt
.venv/bin/python -B customer_release/start.py setup
```

In this example, `python3` must refer to the checked Python 3.12+ executable; substitute its actual path when necessary. Do not install global background software.

## 2. Enter the License key in your own terminal

The setup command checks HTTPS connectivity in the same Python process **before** asking for the key. `NETWORK_PERMISSION_OR_CONNECTION_REQUIRED` means no key has been read and activation has not started. Grant HTTPS access to the actual Python setup command, then rerun it. A working browser or curl request does not grant network permission to that Python command.

At `License key / CDKEY (hidden input):`, paste your License key and press Return. No characters appearing is normal. Enter it in your own terminal, never in the AI chat, URL or command arguments.

Successful activation displays `status: active` and the actual balance for this product in the same response. A fresh, unused test card has 1,000 credits. Previously used or added cards may have a different balance. Installation, activation and balance checks do not spend computation credits.

If you already bought another model, setup adds this purchase to the same local credential rather than replacing it. Each model has separate credits. Default relationship status and computation explicitly select this product regardless of purchase order.

The script stores the access credential in `~/.relationship-compute/Secret/access.json` (directory permissions 700, file 600). The AI invokes the script; it must not open, display or copy the secret file. These permissions restrict other ordinary local users, but cannot hide the credential from software running with your own user permissions. Keep your own backups private. Successful redemption prevents this License key from claiming another credential in our service; it does not destroy the Payhip order record.

If activation is interrupted after key entry, keep the same Secret directory and `activation-pending.json` record. Once connectivity is restored, rerun setup using the original key and directory. Do not delete the record, claim another credential or buy again. The same applies when adding a second purchase. `activate` is a compatibility alias for setup; if you have no new purchase, query status rather than activating again.

## 3. Describe the facts, then confirm

Tell the AI what you actually observed, when it changed, and which explanations remain unverified. It should prepare a fact-check card. Correct anything it misunderstood or omitted before you agree to a calculation.

Only after confirmation may the AI send the necessary numerical factors to Cloudflare. Original relationship text, summaries and confirmations stay locally and are not included in the numerical request. One successful new computation spends one credit. Corrected facts require a new confirmation before a new computation. Valid recovery of the same operation should not spend another credit.

The report gives a model risk index, **not a validated real-world probability of infidelity**. Read information coverage alongside the index: sparse evidence makes the result depend heavily on model defaults. Unverified anomalies remain important leads to investigate; they are not proof of lying or infidelity. No independent case set currently establishes real-world predictive accuracy.

Ask and receive reports in your preferred language. English is the default for the customer guide; this does not mean every language has been tested. The AI follows the full canonical constitution without changing factor meanings or formulas. Quotes must remain exact excerpts of your actual words, not translated replacements.

## Balance, interruptions and old installations

From this package's workers-compute directory:

```sh
.venv/bin/python -B customer_release/start.py status
```

This read-only query also needs HTTPS permission for that Python command. If it returns `NETWORK_ERROR_RETRY_SAME_OPERATION`, check that permission and retry status only; do not reactivate or compute. A failed balance query does not undo an activation that already returned active. Do not delete Secret.

Report only error codes such as `LOCAL_CREDENTIALS_INVALID`, `LOCAL_CONFIGURATION_INVALID` or `ENTITLEMENT_RESPONSE_INVALID` to support. Do not share secrets or screenshots of them.

`expires_at: null` means this credit card has no preset expiry. It is a usage allowance, not a device limit. There is no automatic subscription renewal.

A network interruption during computation may occur after the server has finished. The AI must inspect the case status and request new recovery authorization before using recover with the original request ID, original inputs and original account. Never silently create another paid request. Cached results last 24 hours; HTTP 410 means the cache has expired and requires manual review, not an automatic paid recalculation. Commands and recovery details are in the installed Skill.

If an older installation uses an old API address, use this package's migration command with the original Secret directory:

```sh
.venv/bin/python -B customer_release/start.py migrate
```

It verifies the existing credential before updating the address; failure preserves the original configuration. Do not enter an old License key again. Then run status. Keep unfinished cases with their original package version and request number; do not move them into the new version automatically.

## More credits and support

Purchase link: https://payhip.com/b/pFVqj . The AI may offer the link, but must not pay on your behalf. To add a newly purchased card, keep the existing Secret directory and enter the new key at the hidden prompt:

```sh
.venv/bin/python -B customer_release/start.py redeem
.venv/bin/python -B customer_release/start.py status
.venv/bin/python -B customer_release/start.py help
```

Repeating the same key does not add credits again. An officially connected second product can use `redeem --product <product-id>` and `status --product <product-id>` for its separate allowance. A public Prompt does not by itself mean that product's paid computation is available.

For refunds, missing credentials or order issues: **lppinco@gmail.com**. Include your order number and purchase email, never your License key, access credential, Secret files or private case details. Refunds require manual merchant review. The AI can draft a request; it must not claim it has sent an email, processed a refund or transferred money.

Commands exit automatically. Press Ctrl+C to interrupt, and retain pending records. Tell the AI “stop” to stop the evaluation without new computations.


---

# 中文说明 / Chinese reference

# 关系观察 · 风险分析：开始使用

整理变化，核对线索，再看模型分析。

你已经取得关系模型的使用说明。先完成一次安装和激活，之后直接向 AI 描述情况；它会先整理事实，等你确认后才计算。

## 先确认设备和两样东西

- **设备**：目前在 macOS 上实际验证。AI 需要能读取网页、保存本地文件、运行 Python 3.12 或以上版本，并通过 HTTPS 联网。Linux 尚未实机验证；Windows 暂不支持。仅能聊天的工具不能使用本程序。无需安装 MCP、浏览器扩展或后台常驻连接器。
- **激活码**：Payhip 订单中标为 License key 的唯一代码。`Product Key: pFVqj` 是商品编号，不能用于激活。
- **本包**：完整保留解压后的文件，包括隐藏的 `.agents` 目录。服务地址已内置，无需填写或替换。

## 第一步：请 AI 准备环境

把这段话交给能操作本地文件的 AI：

> 请读取本说明和项目 `.agents/skills/relationship-evaluator/SKILL.md`，只准备关系模型。先检查实际使用的 Python 是否为 3.12 或以上版本，说明下载、安装和本地操作，并按需要申请文件与联网权限。按下面的命令准备环境，不安装全局后台软件。先不要计算。

没有 Skill 功能的客户端也可以直接读取这些文件。默认 `python3` 版本不足时，使用已经安装的 Python 3.12+ 的实际路径；没有可用版本时先说明如何从官方来源安装，取得安装授权后再继续。不要替换 macOS 系统 Python。

## 第二步：在自己的终端激活

AI 按下面的操作说明准备环境并引导启动隐藏输入。出现 `CDKEY` 提示后，**你在自己电脑的终端粘贴 License key 并按回车**。看不到输入字符是正常现象。不要把码发到聊天里或放进命令参数。

成功后显示 `status: active` 和本商品余额。首次未使用的这张测试卡应有 1000 次；已使用或追加过卡时，以实际返回为准。安装、激活和查询余额不扣计算次数。

## 第三步：描述情况，核对后再计算

告诉 AI 你实际观察到的行为、发生变化的时间，以及哪些解释尚未核实。AI 会给出事实核验卡；听错、遗漏或需要补充的地方，可以直接更正。

你确认事实并同意计算后，AI 才发送必要的数值因子到云端，成功的新计算扣 1 次。关系案例原文、摘要和确认留在本机，不随数值请求上传。停止时告诉 AI“停止”。

报告给出模型风险指数，并非已验证的现实出轨概率。信息很少时结果会大量依赖默认设定；请同时看信息覆盖率。尚未核实的异常保留为重要线索，不能直接写成已证实的说谎或越轨。目前没有独立案例集证明真实预测准确率。

## 需要安装命令或遇到问题时

以下是供 AI 和排错使用的操作说明。顾客不需要先记住所有命令。

当前商品是独立 1000 次卡，无预设到期日、不自动续费，以实际权益查询结果为准。内置服务为 `https://api.ainative.us.ci`；原计算入口已关闭，不要换成旧地址。

### 安装与激活命令

完整解压ZIP并保留其中隐藏的 `.agents` 目录。让AI读取本说明和项目 `.agents/skills/relationship-evaluator/SKILL.md`。即使客户端没有Skill功能，也可直接读取这两份文件。AI应先说明需要的文件权限、网络请求和安装内容，再在当前项目内准备环境，不安装全局后台软件：

```sh
cd "/解压项目绝对路径/workers-compute"
python3 -m venv .venv
.venv/bin/python -m pip install -r customer_release/requirements.txt
.venv/bin/python -B customer_release/start.py setup
```

准备购买权益时，脚本先用**同一 Python 进程**检查服务连通性；如果联网权限或连接不可用，会在要求输入 CDKEY **之前**报 `NETWORK_PERMISSION_OR_CONNECTION_REQUIRED`。AI 应为实际 `start.py setup` 命令申请联网权限，再运行它；网页或其他命令能联网不代表本命令已获准。通过检查后，顾客只在终端隐藏输入本次购买所得 CDKEY，不把它粘进聊天或命令参数。没有凭证时脚本创建凭证；如果先购买了写作等其他模型，则将本张关系卡追加到同一个凭证，不替换原配置。成功的同一响应会直接显示 `status: active` 和本商品剩余次数，不再为显示余额发起第二次请求。脚本将访问凭证保存到 `~/.relationship-compute/Secret/access.json`，目录权限700、文件600；AI负责调用脚本，不读取秘密文件。首次激活请求中断或响应丢失时，保留 `activation-pending.json`，在同一目录、联网权限就绪后用**原 CDKEY**重试，不要删掉记录重新领取。追加权益中断时也在原目录用原 CDKEY 重试 setup；不会重复加额度。

本版的 `activate` 是 `setup` 的兼容别名，也会要求隐藏输入本次购买的 CDKEY。已有授权、没有新卡时直接运行 `status`，不重复激活。默认 `status` 和关系计算明确选择本包的关系商品，不依赖首次购买的是哪个模型。

已经用旧版包激活的顾客，先用本包在原来的Secret目录运行 `.venv/bin/python -B customer_release/start.py migrate`。脚本用原凭证向新地址查询余额，成功后才原子更新本地服务地址；失败时保留旧配置、不再次输入CDKEY。成功后运行 `status` 再核对一次余额，然后继续原案例。不要打开或复制Secret文件。

Secret权限限制同机其他普通用户读取，不能阻止当前用户权限下的AI或恶意程序读取；不要把它当作对宿主AI完全不可见的保险箱。备份只由顾客自己保管，不上传聊天或公开网盘。成功兑换后CDKEY不能再次领取本服务凭证；它在Payhip平台的订单记录中仍然存在，并非被平台销毁。

### 查询、日常使用与恢复

告诉AI：“读取此项目的使用说明，按原4.2模型帮我梳理，先核对摘要，等我确认后计算。”AI按Skill管理案例，使用 `case_session.py compute --credentials-directory "$HOME/.relationship-compute/Secret"`。原文、摘要和确认留在本机；只有数值因子发送给服务端。

查询余额或到期时间：

```sh
.venv/bin/python -B customer_release/start.py status
```

这条命令也会向云端发起 HTTPS 请求。在限制终端联网的 AI 客户端中，先为**这条 Python status 命令本身**申请网络权限；网页能打开或 `curl /health` 成功，不代表 Python 命令已有权限。若返回 `NETWORK_ERROR_RETRY_SAME_OPERATION`，先核对权限，再只重试 status；不要重新输入 CDKEY 或发起计算。status 查询不扣次。

如果首次激活已显示 `status: active` 和剩余次数，激活就已完成；之后查询余额失败不会撤销激活。不要再次提交CDKEY，也不要删除Secret目录。遇到 `LOCAL_CREDENTIALS_INVALID`、`LOCAL_CONFIGURATION_INVALID` 或 `ENTITLEMENT_RESPONSE_INVALID`，只把错误码提供给商户支持；不要发送密钥、Secret文件或截图。新版会区分本机凭证问题、服务响应格式问题和网络问题，避免都显示为笼统错误。

`expires_at: null` 表示当前次数卡未设到期时间。按次消耗，不是设备数量限制。网络中断可能代表服务端已算完；AI先读案例 `status`，得到新的恢复授权后用 `recover` 沿用原请求编号，不得换编号或换账户自动再算一次。结果缓存24小时，过期返回410，须人工核对，不自动再次扣次。

### 续购与人工售后

```sh
.venv/bin/python -B customer_release/start.py help
```

购买页面： https://payhip.com/b/pFVqj 。AI只提供购买入口，不代付款。购买本商品的新次数卡后，沿用原Secret目录，在终端隐藏输入新CDKEY追加次数：

```sh
.venv/bin/python -B customer_release/start.py redeem
```

成功后再次运行`status`核对余额；同一CDKEY重复提交不会重复加次数。其他模型商品若已正式接入，可用`redeem --product <商品ID>`追加到同一个访问凭证，再用`status --product <商品ID>`查询其独立额度。顾客不需要把新CDKEY粘进聊天或保存到Secret。当前没有自动订阅续期；未公布的新模型商品即使有Prompt，也不能据此推断其计算服务已上线。

退款、丢失凭证或订单问题，联系人工售后 **lppinco@gmail.com**，提供订单号和购买邮箱，不发送访问凭证。当前没有自动发邮件、自动退款或资金转移工具；AI可以帮助拟好申请内容，但不能声称已发送或已退款。

命令完成会自动退出。中止可按Ctrl+C；不要删除中断记录。停止评估时告诉AI“停止”，不再发起计算。
