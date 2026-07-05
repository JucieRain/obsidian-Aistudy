---
title: "抖音一键入Obsidian：Douyin Capture插件"
source: https://mp.weixin.qq.com/s/o4CDGEmLobzTuxC1E2sMSw
date: 2026-07-05
fetched: 2026-07-05
tags: ["Obsidian", "插件", "抖音", "Whisper", "内容管理"]
referenced_by: ["[[wiki/tools/Douyin Capture]]"]
---

# 抖音一键入 Obsidian——打工人刷到好视频，3 步沉到自己的内容库

> 原文链接：https://mp.weixin.qq.com/s/o4CDGEmLobzTuxC1E2sMSw

## 痛点

内容创作者 90% 的痛点不是「看不到好东西」，是「看到 → 留下」的链路断了。官方下载有水印，复制粘贴丢信息，多端存储难整理。

## Douyin Capture 插件

核心能力：
1. 提取文案：Whisper 转写 + 提取描述配文
2. 提取视频：仅下载无水印视频
3. 链接形式全覆盖：短链、长链、分享码、分享文案
4. 全部数据本机处理，无需 Cookie 或付费 API

## 使用步骤

### 第 1 步：启动本地后端
```bash
git clone https://github.com/lyxdream/obsidian-content-capture-backend.git
cd obsidian-content-capture-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python web/app.py
```
默认监听 http://127.0.0.1:5050

### 第 2 步：安装插件
从 Releases 下载 → 解压到 .obsidian/plugins/douyin-capture/ → 启用

### 第 3 步：使用
点击 ribbon 图标 → 粘贴分享链接 → 选择模式 → 笔记自动生成

## 使用场景
- 内容选题池：23 条视频 2 小时全部抓取转写，15 分钟筛出 6 个选题
- 竞品研究：按博主分文件夹，全文搜索找灵感
- 方法论学习：转写后精读 + 个人反思
- 灵感碎片池：一句话灵感直接丢入

## 限制
- 仅支持 Obsidian 桌面版 1.4.0+
- Whisper 模型首次下载 1-2GB
- 不适合一次性临时抓取
