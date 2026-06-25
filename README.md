[简体中文](https://github.com/vu1Art1st/magnetos/blob/main/README_CN.md) | English

> Foreword: This project is primarily modified with the help of AI based on the original author's work, tailored to my own needs for use in CTF competitions.

# magnetos
Original repository: https://github.com/restran/magnetos
A toolkit to accelerate your puzzle solving in CTF competitions.

<div style="max-width: 270px; margin: 0 auto; ">
<img src="docs/icon/magnetos.png" style="margin: 0 auto; max-width: 270px; display: block;">
</div>

## Third-party Dependencies

The following tools are required when running `what_steg`:

- [zsteg](https://github.com/zed-0xff/zsteg)
- pngcheck
- exiftool

```
apt install pngcheck
apt install libimage-exiftool-perl
gem install zsteg
```

## Installation

    pip3 install magnetos

## Usage

Use the `magnetos.py` entry script:

    python magnetos.py <subcommand> [args...]

Or invoke directly via Python module:

    python -m magnetos.fuzzing.what_encode -h

## Tools Provided

- **what_format** — Similar to binwalk and foremost, but can extract additional file types such as psd
- **what_code_scheme** — Detect encoding type
- **what_encode** — Automatically detect file encoding and perform fuzzing
- **what_steg** — Automated steganography puzzle solver
- **web_get** — Automatically download all resources from a given URL to local
- **file_hash** — Calculate file hash
- **file_strings** — Same as the strings command, but automatically filters out \0
- **find_ctf_flag** — Search for possible flags in text files or directories based on flag patterns
- **reverse_proxy** — Reverse proxy
- **steg_hide_cracker** — Brute-force steghide passwords

## Changelog

### v0.8.0 (2026-06-17)

- **Removed stegdetect external binary dependency**: `what_steg` now uses the pure Python implementation [stegdetect-py](https://github.com/vu1Art1st/stegdetect-py) to replace the original C `stegdetect` command-line tool
- **New dependencies**: `numpy>=1.22`, `scipy>=1.8`
- **Python 3 modernization**: Removed all Python 2 compatibility code (`from __future__`, `# -*- coding`, `PY2`/`PY3` branches)
- **Dependency cleanup**: Removed the `future` package, no longer depends on the Python 2 compatibility layer
- **Build system**: Deleted `setup.py`, fully migrated to `pyproject.toml`, using `uv` for dependency management
- **Invocation method**: No longer registers system-level CLI commands; unified usage via `python magnetos.py <subcommand>` entry point
- **Module interoperability**: `what_steg` no longer calls `what_format` via subprocess, now uses direct Python import invocations
- **Output directory**: Unified output to `output/{filename}/` directory (`what_steg`, `what_format`, `web_get`)
- Added missing `requests` dependency to `requirements.txt`

### v0.7.0

- Initial release
