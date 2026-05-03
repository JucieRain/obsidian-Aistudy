#!/usr/bin/env python3
"""
Pandoc DOCX to Markdown 后处理脚本 (简化版)

修复问题：
1. 标题层级：将 **标题** 转换为 ## 标题
2. 图片尺寸：移除 Pandoc 的 {width="..." height="..."} 参数
3. 多余空行清理

使用方法：
    python pandoc_postprocess.py input.md output.md
"""

import re
import sys
from pathlib import Path


def fix_headings(content: str) -> str:
    """
    修复标题层级

    Pandoc 将标题转换为 **标题** 格式，需要修复为 Markdown 标题格式
    """
    lines = content.split('\n')
    fixed_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 检测 **内容** 格式的标题行（前后可能有空行）
        match = re.match(r'^\*\*([^*]+)\*\*$', stripped)
        if match:
            title_content = match.group(1)

            # 判断层级
            # "2.1 原理" 格式 -> 三级标题
            if re.match(r'^\d+\.\d+\s', title_content):
                fixed_lines.append(f'### {title_content}')
            # 其他 -> 二级标题
            else:
                fixed_lines.append(f'## {title_content}')
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def fix_images(content: str) -> str:
    """
    修复图片链接

    移除 Pandoc 添加的尺寸参数：{width="5.75in" height="3.14in"}
    """
    # 移除尺寸参数
    content = re.sub(r'\{width="[^"]*"\s+height="[^"]*"\}', '', content)

    return content


def clean_extra_lines(content: str) -> str:
    """
    清理多余空行
    """
    # 最多保留两个连续空行
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    return content


def postprocess(input_path: Path, output_path: Path):
    """
    执行后处理
    """
    print(f"读取: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 执行修复
    print("执行后处理...")
    content = fix_headings(content)
    content = fix_images(content)
    content = clean_extra_lines(content)

    # 写入输出
    print(f"写入: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("完成!")


def main():
    if len(sys.argv) < 2:
        print("使用方法: python pandoc_postprocess.py input.md [output.md]")
        print("示例: python pandoc_postprocess.py doc.md doc_fixed.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"错误: 文件不存在 - {input_path}")
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_name(input_path.stem + '_fixed.md')

    postprocess(input_path, output_path)


if __name__ == '__main__':
    main()