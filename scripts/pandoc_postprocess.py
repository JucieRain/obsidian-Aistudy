#!/usr/bin/env python3
"""
Pandoc DOCX → Markdown 后处理脚本

修复问题：
1. 标题层级：将 **标题** 转换为 ## 标题
2. 代码块：将 Pandoc Grid table 格式转换为 fenced code blocks
3. 转义字符：处理反斜杠转义

使用方法：
    python pandoc_postprocess.py input.md output.md
    python pandoc_postprocess.py input.md  # 输出到 input_fixed.md
"""

import re
import sys
from pathlib import Path


def fix_headings(content: str) -> str:
    """
    修复标题层级

    规则：
    - **🎯 系统目标** → ## 🎯 系统目标
    - **2.1 原理** → ### 2.1 原理
    - **Skills 资源合集** → ## Skills 资源合集
    """
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        # 匹配被 ** 包围的标题行
        # 格式：**内容** 或 **数字.数字 内容**
        match = re.match(r'^\*\*([^*]+)\*\*$', line.strip())
        if match:
            title_content = match.group(1)

            # 判断标题层级
            # 格式如 "2.1 原理" 或 "3.4 提示词写法" → 三级标题
            if re.match(r'^\d+\.\d+\s', title_content):
                fixed_lines.append(f'### {title_content}')
            # 格式如 "第一步：摄取" 或带 emoji 的主标题 → 二级标题
            else:
                fixed_lines.append(f'## {title_content}')
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def fix_code_blocks(content: str) -> str:
    """
    修复代码块

    Pandoc 将代码块转换为：
      ---------------------------------------------------------------------------
      Plain Text\
      内容\
      ---------------------------------------------------------------------------

    需要转换为：
      ```plaintext
      内容
      ```
    """
    lines = content.split('\n')
    fixed_lines = []

    in_code_block = False
    code_lang = ''
    code_content = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # 检测代码块开始（以多个 - 开头的分隔线）
        if re.match(r'^\s*-{20,}\s*$', line):
            # 检查下一行是否是语言标识
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()

                # 常见语言标识
                lang_patterns = [
                    ('Plain Text', 'plaintext'),
                    ('YAML', 'yaml'),
                    ('Markdown', 'markdown'),
                    ('Python', 'python'),
                    ('Bash', 'bash'),
                    ('Shell', 'shell'),
                    ('JSON', 'json'),
                    ('JavaScript', 'javascript'),
                    ('HTML', 'html'),
                    ('CSS', 'css'),
                    ('SQL', 'sql'),
                ]

                detected_lang = None
                for pattern, lang in lang_patterns:
                    if next_line.startswith(pattern) or next_line == pattern:
                        detected_lang = lang
                        # 如果行只有语言标识，跳过它
                        if next_line == pattern or re.match(r'^' + pattern + r'\\?\s*$', next_line):
                            i += 1
                        break

                if detected_lang:
                    in_code_block = True
                    code_lang = detected_lang
                    code_content = []
                    i += 1
                    continue

        # 检测代码块结束
        if in_code_block and re.match(r'^\s*-{20,}\s*$', line):
            # 输出修复后的代码块
            fixed_lines.append(f'```{code_lang}')
            for code_line in code_content:
                # 处理转义字符
                fixed_line = code_line.rstrip('\\')
                fixed_lines.append(fixed_line)
            fixed_lines.append('```')
            fixed_lines.append('')

            in_code_block = False
            code_lang = ''
            code_content = []
            i += 1
            continue

        # 收集代码块内容
        if in_code_block:
            code_content.append(line)
        else:
            fixed_lines.append(line)

        i += 1

    return '\n'.join(fixed_lines)


def fix_escape_chars(content: str) -> str:
    """
    修复转义字符

    Pandoc 会转义特殊字符：
    - \\-\\-\\- → ---
    - \\| → |
    - \\# → #
    - 反斜杠 → 正常字符
    """
    # 修复 YAML frontmatter 中的转义
    content = re.sub(r'\\-\--', '---', content)
    content = re.sub(r'\\|', '|', content)
    content = re.sub(r'\\#', '#', content)

    # 修复其他常见转义（在代码块外）
    # 注意：这个操作要谨慎，避免破坏代码块内的内容

    return content


def fix_image_links(content: str, media_path: str = None) -> str:
    """
    修复图片链接

    Pandoc 输出：
    ![](Clippings/pandoc_media/media/image1.png){width="5.75in" height="3.1458333333333335in"}

    转换为 Obsidian 格式：
    ![[image1.png]]
    或保留相对路径：
    ![](media/image1.png)
    """
    # 移除 Pandoc 的尺寸参数
    content = re.sub(r'\{width="[^"]*" height="[^"]*"\}', '', content)

    # 可选：转换为 Obsidian wikilink 格式
    # content = re.sub(r'!\[\]\([^)]*media/([^)]+)\)', f'![[\\1]]', content)

    return content


def fix_lists(content: str) -> str:
    """
    修复列表格式

    Pandoc 有时会将列表转换为表格或段落
    """
    # 检测数字列表模式并修复
    # 这个比较复杂，暂时不做

    return content


def postprocess(content: str) -> str:
    """
    执行所有后处理步骤
    """
    # 1. 修复代码块（优先处理，避免影响其他步骤）
    content = fix_code_blocks(content)

    # 2. 修复标题层级
    content = fix_headings(content)

    # 3. 修复转义字符
    content = fix_escape_chars(content)

    # 4. 修复图片链接
    content = fix_image_links(content)

    # 5. 清理多余空行
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def main():
    if len(sys.argv) < 2:
        print("使用方法: python pandoc_postprocess.py input.md [output.md]")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        # 默认输出到 input_fixed.md
        output_path = input_path.with_name(input_path.stem + '_fixed.md')

    # 读取输入文件
    print(f"读取: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 执行后处理
    print("执行后处理...")
    fixed_content = postprocess(content)

    # 写入输出文件
    print(f"写入: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print("完成!")

    # 输出统计
    orig_lines = len(content.split('\n'))
    fixed_lines = len(fixed_content.split('\n'))
    print(f"原始行数: {orig_lines}, 处理后: {fixed_lines}")


if __name__ == '__main__':
    main()