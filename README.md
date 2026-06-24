>写在前面：本项目主要是利用AI在原作者的基础上，按照自己的需求进行修改，以便于在CTF比赛中使用。

# magnetos
原仓库链接：https://github.com/restran/magnetos
一款帮你在 CTF 比赛中加速解题的工具

<div style="max-width: 270px; margin: 0 auto; ">
<img src="docs/icon/magnetos.png" style="margin: 0 auto; max-width: 270px; display: block;">
</div>

## 依赖的第三方工具

以下工具在运行 `what_steg` 时需要：

- [zsteg](https://github.com/zed-0xff/zsteg)
- pngcheck
- exiftool

```
apt install pngcheck
apt install libimage-exiftool-perl
gem install zsteg
```

## 安装方法

    pip3 install magnetos

## 运行方式

使用 `magnetos.py` 入口脚本：

    python magnetos.py <子命令> [参数...]

或通过 Python 模块直接调用：

    python -m magnetos.fuzzing.what_encode -h

## 提供的工具

- **what_format** — 类似 binwalk 和 foremost，但可以分离出一些其他文件，例如 psd
- **what_code_scheme** — 检测编码类型
- **what_encode** — 自动检测文件编码并进行模糊测试
- **what_steg** — 隐写题目自动化解题工具
- **web_get** — 自动下载指定 URL 的所有资源到本地
- **file_hash** — 计算文件 hash
- **file_strings** — 与 strings 命令相同，但是会自动过滤掉 \0
- **find_ctf_flag** — 根据 flag 特征从文本文件或目录中查找可能的 flag
- **reverse_proxy** — 反向代理
- **steg_hide_cracker** — 爆破 steghide 密码

## 版本记录

### v0.8.0 (2026-06-17)

- **移除 stegdetect 外部二进制依赖**：`what_steg` 现使用纯 Python 实现的 [stegdetect-py](https://github.com/abeluck/stegdetect) 替代原有的 C 语言 `stegdetect` 命令行工具
- **新增依赖**：`numpy>=1.22`、`scipy>=1.8`
- **Python 3 现代化**：移除所有 Python 2 兼容代码（`from __future__`、`# -*- coding`、`PY2`/`PY3` 分支）
- **依赖清理**：移除 `future` 包，不再依赖 Python 2 兼容层
- **构建系统**：删除 `setup.py`，全面迁移至 `pyproject.toml`，使用 `uv` 管理依赖
- **运行方式**：不再注册系统级 CLI 命令，统一使用 `python magnetos.py <子命令>` 入口
- **模块互调**：`what_steg` 不再通过子进程调用 `what_format`，改为直接 Python import 调用
- **输出目录**：统一输出到 `output/{文件名}/` 下（`what_steg`、`what_format`、`web_get`）
- 补充 `requirements.txt` 缺失的 `requests` 依赖

### v0.7.0

- 初始发布版本
