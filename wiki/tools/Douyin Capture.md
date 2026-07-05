---
title: Douyin Capture
created: 2026-07-05
updated: 2026-07-05
sources: ["[[Clippings/articles/抖音一键入Obsidian：Douyin Capture插件.md]]"]
tags: [工具, Obsidian插件, 抖音, Whisper, 内容管理]
status: stable
---

# Douyin Capture

> Obsidian 插件，将抖音分享链接转化为结构化笔记：无水印下载 + Whisper 转写 + 自动化入库

## 核心能力

| 能力 | 说明 |
|------|------|
| 提取文案 | Whisper 语音转写 + 提取描述配文 |
| 提取视频 | 仅下载无水印视频 |
| 链接全覆盖 | 短链、长链、分享码、分享文案 |
| 隐私 | 全部数据本机处理，无需 Cookie 或付费 API |

## 与替代方案对比

| 维度 | Douyin Capture | 抖音收藏 | 微信传输 |
|------|---------------|----------|----------|
| 视频画质 | 无水印 | 有水印 | 有水印 |
| 文案提取 | 自动 | ❌ | ❌ |
| 视频转文字 | 本地 Whisper | ❌ | ❌ |
| 隐私 | 本机处理 | 云端 | 云端 |
| 结构笔记 | ✅ | ❌ | ❌ |

## 安装

1. 启动后端：`git clone → venv → pip install → python web/app.py`（监听 127.0.0.1:5050）
2. 安装插件：Releases 下载 → 解压到 `.obsidian/plugins/douyin-capture/` → 启用
3. 首次使用自动下载 Whisper 模型（1-2GB）

## 使用场景

- **内容选题池**：批量抓取转写，15 分钟筛选题
- **竞品研究**：按博主分文件夹，全文搜索
- **方法论学习**：转写后精读 + 反思
- **灵感碎片池**：一句话灵感直接丢入

## 限制

- 仅支持 Obsidian 桌面版 1.4.0+
- 不适合一次性临时抓取（后端 + 模型太重）

> — [[Clippings/articles/抖音一键入Obsidian：Douyin Capture插件.md]]

## 参见

- [[tools/Obsidian]]
