---
title: Claude Code
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Claude Code 国内丝滑部署指南.md]]"
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
tags: [工具, AI编程, Anthropic, 终端]
status: stable
---

# Claude Code

> Anthropic 推出的终端 AI 编程助手，可直接在命令行与 AI 协作写代码

## 核心特性

- **终端集成**：在命令行直接使用，适合习惯 Git、编辑器的开发者
- **项目理解**：能读取项目文件，理解代码结构
- **多平台支持**：Windows (WSL/Git Bash)、macOS、Linux
- **原生安装**：自包含可执行文件，不依赖 Node.js

## 安装方式

### 原生安装（推荐）

```bash
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Homebrew
brew install --cask claude-code
```

### NPM 安装（需 Node.js 18+）

```bash
npm install -g @anthropic-ai/claude-code
```

## 配置要点

配置文件位置：
- Windows: `C:\Users\用户名\.claude\settings.json`
- Mac/Linux: `~/.claude/settings.json`

关键配置项：
- `ANTHROPIC_AUTH_TOKEN` - API 认证令牌
- `ANTHROPIC_BASE_URL` - API 服务地址
- `ANTHROPIC_MODEL` - 主模型 ID
- `ANTHROPIC_SMALL_FAST_MODEL` - 快速小模型

## 常见问题

| 问题 | 解决方案 |
|-----|---------|
| 命令找不到 | 检查 PATH 环境变量，重启终端 |
| Invalid API Key | 检查配置文件路径和令牌格式 |
| offline 状态 | 不影响使用，仅表示无法连接 Google |
| fetch failed | 检查网络代理配置 |

## 在知识库中的应用

Claude Code 是 Karpathy LLM Wiki 方法的核心工具：
- 自动维护 wiki/ 目录结构
- 执行素材录入、健康检查等操作
- 创建概念/工具/人物页面
- 更新 index.md 和 log.md

## 参见

- [[concepts/第二大脑]]
- [[concepts/LLM Wiki]]
- [[tools/Obsidian]]
- [[people/Karpathy]]

## 来源

- [[Clippings/articles/Claude Code 国内丝滑部署指南.md]]
- [[Clippings/articles/Obsidian + Claude Code 教程.md]]