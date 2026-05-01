#!/bin/bash
# Wiki 搜索脚本 - 替代 QMD 的简单搜索工具
# 用法: wiki-search.sh <关键词> [限制数量]

WIKI_DIR="wiki/"
LIMIT=${2:-20}

if [ -z "$1" ]; then
    echo "用法: wiki-search.sh <关键词> [限制数量]"
    exit 1
fi

# 搜索 wiki 目录中的 markdown 文件
grep -ril "$1" "$WIKI_DIR" 2>/dev/null | head -$LIMIT