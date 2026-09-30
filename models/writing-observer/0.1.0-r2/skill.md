---
name: writing-observer
description: 用作者目标和原文证据讨论可选的写作方向；付费自测调用写作计算服务。
---

读取安装目录 `writing-observer/PROMPT.md` 和 `writing-observer/START.md`。先问作者目标和文体；调用 `writing-observer/start.py` 前说明上传片段与扣次，等作者确认。只让顾客在终端隐藏输入 CDKEY；不要读取或输出 Secret。服务端返回候选观察后，逐字核对原文，由作者决定是否修改。不得给统一质量分数或自动改写。
