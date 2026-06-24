#!/usr/bin/env python3
"""
magnetos - CTF 自动化解题工具集

用法:
    python magnetos.py <子命令> [参数...]

子命令:
    what_steg        隐写题目全自动解题
    what_encode      编码自动识别与递归解码
    what_format      按文件魔数分离嵌入文件
    what_code_scheme 检测编码类型
    find_ctf_flag    目录/文件中查找 flag
    web_get          网站资源下载
    steg_hide_cracker steghide 密码爆破
    file_hash        计算文件哈希
    file_strings     提取可打印字符串
    reverse_proxy    反向代理
"""

import sys

SUBCOMMANDS = {
    'what_steg':        ('magnetos.fuzzing.what_steg', 'main'),
    'what_encode':      ('magnetos.fuzzing.what_encode', 'main'),
    'what_format':      ('magnetos.fuzzing.what_format', 'main'),
    'what_code_scheme': ('magnetos.fuzzing.what_code_scheme', 'main'),
    'find_ctf_flag':    ('magnetos.utils.find_ctf_flag', 'main'),
    'web_get':          ('magnetos.utils.web_get', 'main'),
    'steg_hide_cracker':('magnetos.cracker.steg_hide_cracker', 'main'),
    'file_hash':        ('magnetos.utils.file_hash', 'main'),
    'file_strings':     ('magnetos.utils.file_strings', 'main'),
    'reverse_proxy':    ('magnetos.proxy.reverse_proxy', 'main'),
}

HELP_TEXT = __doc__


def print_help():
    print(HELP_TEXT)


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    subcommand = sys.argv[1]

    if subcommand in ('-h', '--help', 'help'):
        print_help()
        sys.exit(0)

    if subcommand not in SUBCOMMANDS:
        print(f"未知子命令: {subcommand}\n")
        print_help()
        sys.exit(1)

    # 将 sys.argv 修改为只包含子命令之后的参数
    # 这样各模块内的 parser.parse_args() 就能正常工作
    module_path, func_name = SUBCOMMANDS[subcommand]
    sys.argv = [f'magnetos {subcommand}'] + sys.argv[2:]

    import importlib
    module = importlib.import_module(module_path)
    func = getattr(module, func_name)
    func()


if __name__ == '__main__':
    main()
