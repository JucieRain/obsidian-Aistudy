#!/usr/bin/env python3
"""
PDF文本提取脚本
使用方法：
  1. 先安装pypdf: pip install pypdf
  2. 运行此脚本: python extract_pdf.py

或者一行命令：
  pip install pypdf && python -c "from pypdf import PdfReader; r=PdfReader('OpenClaw橙皮书-从入门到精通-v1.3.1.pdf'); open('output.md','w',encoding='utf-8').write('\\n'.join([p.extract_text() for p in r.pages]))"
"""

import os
import sys
from pathlib import Path

def extract_pdf(pdf_path, output_path):
    """提取PDF文本并保存为Markdown"""
    try:
        from pypdf import PdfReader
    except ImportError:
        print("请先安装pypdf: pip install pypdf")
        sys.exit(1)

    print(f"读取PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"总页数: {total_pages}")

    text_parts = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            text_parts.append(f"## 第 {i+1} 页\n\n{text}\n")
        if (i + 1) % 20 == 0:
            print(f"已处理: {i+1}/{total_pages} 页")

    print(f"\n写入文件: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# PDF提取内容\n\n> 来源: {pdf_path}\n> 总页数: {total_pages}\n\n")
        f.write('\n'.join(text_parts))

    print(f"完成! 共提取 {total_pages} 页")

def main():
    # PDF文件列表
    pdf_dir = Path("Clippings/papers")
    pdfs = [
        "OpenClaw橙皮书-从入门到精通-v1.3.1.pdf",
        "OpenClaw 完全指南（花园版）！.pdf",
        "【杨彧鑫AI】OpenClaw蓝皮书-1.0.0版.pdf"
    ]

    print("=" * 50)
    print("OpenClaw PDF 文档提取工具")
    print("=" * 50)

    for pdf_name in pdfs:
        pdf_path = pdf_dir / pdf_name
        if pdf_path.exists():
            output_name = pdf_name.replace('.pdf', '.md')
            output_path = pdf_dir / output_name
            print(f"\n{'='*50}")
            extract_pdf(str(pdf_path), str(output_path))
        else:
            print(f"\n跳过: {pdf_name} (文件不存在)")

if __name__ == "__main__":
    main()