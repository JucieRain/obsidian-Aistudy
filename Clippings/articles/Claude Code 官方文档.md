---
title: "Claude Code 官方文档"
source: "https://code.claude.com/docs/en/overview"
author:
  - "[[Anthropic]]"
published:
created: 2026-04-22
description: "Claude Code 官方文档，包含安装、配置、使用方法"
tags:
  - "clippings"
  - "official"
---

# Claude Code 官方文档

> Anthropic 官方维护的 Claude Code 文档站点

## 文档地址

- **总览**: https://code.claude.com/docs/en/overview
- **安装**: https://code.claude.com/docs/en/installation
- **配置**: https://code.claude.com/docs/en/configuration
- **使用指南**: https://code.claude.com/docs/en/usage

## 核心内容

### 安装方式

官方支持三种安装方式：

| 方式 | 命令 | 适用系统 |
|-----|------|---------|
| **原生安装** | `curl -fsSL https://claude.ai/install.sh | bash` | macOS/Linux/WSL |
| **PowerShell** | `irm https://claude.ai/install.ps1 | iex` | Windows |
| **Homebrew** | `brew install --cask claude-code` | macOS |
| **npm** | `npm install -g @anthropic-ai/claude-code` | 需Node.js 18+ |

### 配置要点

配置文件位置：
- Windows: `C:\Users\用户名\.claude\settings.json`
- macOS/Linux: `~/.claude\settings.json`

核心配置项：
- `ANTHROPIC_AUTH_TOKEN` - API认证令牌
- `ANTHROPIC_BASE_URL` - API服务地址
- `ANTHROPIC_MODEL` - 主模型ID
- `ANTHROPIC_SMALL_FAST_MODEL` - 快速小模型

### 主要功能

- 终端集成：命令行直接使用
- 项目理解：读取项目文件，理解代码结构
- 多平台支持：Windows/Mac/Linux
- MCP集成：扩展工具能力
- Skills系统：自定义工作流

## 参见

- [[wiki/tools/Claude Code]] - 工具详情页
- [[wiki/practices/工具模型配置汇总]] - 模型配置方法
- [[wiki/tools/cc-switch]] - 国产模型切换工具

## 来源

- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/installation