# 开始使用

这是原4.2版本的顾客交付包。不需要MCP、浏览器扩展或后台常驻连接器。需要能读取本地文件、执行Python并访问HTTPS的AI客户端，以及macOS或Linux、Python 3.12及以上。macOS已实际验证；Linux尚未实机验证；当前不支持Windows文件锁。只能聊天、不能运行代码或联网请求的客户端不能使用此程序。

本包已接入云端服务 `https://api.loopinco.qzz.io`，目前供首轮顾客流程验收使用。服务地址已内置，不需要顾客填写；原计算入口已关闭，不要替换为旧地址。当前商品为独立1000次卡，不设到期时间；以激活后的查询结果为准。

## 一次性准备

完整解压ZIP并保留其中隐藏的 `.agents` 目录。让AI读取本说明和项目 `.agents/skills/relationship-evaluator/SKILL.md`。即使客户端没有Skill功能，也可直接读取这两份文件。AI应先说明需要的文件权限、网络请求和安装内容，再在当前项目内准备环境，不安装全局后台软件：

```sh
cd "/解压项目绝对路径/workers-compute"
python3 -m venv .venv
.venv/bin/python -m pip install -r customer_release/requirements.txt
.venv/bin/python -B customer_release/start.py activate
```

首次激活只需顾客在终端隐藏输入购买所得CDKEY。不要把CDKEY粘进聊天或命令参数。成功输出 `status: active` 和剩余次数。脚本将访问凭证保存到 `~/.relationship-compute/Secret/access.json`，目录权限700、文件600；AI负责调用脚本，不读取秘密文件。激活中断时保留 `activation-pending.json`，在同一目录重试可恢复，不要删掉它重新领取。

已经用旧版包激活的顾客，先用本包在原来的Secret目录运行 `.venv/bin/python -B customer_release/start.py migrate`。脚本用原凭证向新地址查询余额，成功后才原子更新本地服务地址；失败时保留旧配置、不再次输入CDKEY。成功后运行 `status` 再核对一次余额，然后继续原案例。不要打开或复制Secret文件。

Secret权限限制同机其他普通用户读取，不能阻止当前用户权限下的AI或恶意程序读取；不要把它当作对宿主AI完全不可见的保险箱。备份只由顾客自己保管，不上传聊天或公开网盘。成功兑换后CDKEY不能再次领取本服务凭证；它在Payhip平台的订单记录中仍然存在，并非被平台销毁。

## 日常使用

告诉AI：“读取此项目的使用说明，按原4.2模型帮我梳理，先核对摘要，等我确认后计算。”AI按Skill管理案例，使用 `case_session.py compute --credentials-directory "$HOME/.relationship-compute/Secret"`。原文、摘要和确认留在本机；只有数值因子发送给服务端。

查询余额或到期时间：

```sh
.venv/bin/python -B customer_release/start.py status
```

`expires_at: null` 表示当前次数卡未设到期时间。按次消耗，不是设备数量限制。网络中断可能代表服务端已算完；AI先读案例 `status`，得到新的恢复授权后用 `recover` 沿用原请求编号，不得换编号或换账户自动再算一次。结果缓存24小时，过期返回410，须人工核对，不自动再次扣次。

## 续购与售后

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
