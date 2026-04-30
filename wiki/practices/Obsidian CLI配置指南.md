---
title: Obsidian CLI配置指南
created: 2026-04-30
updated: 2026-04-30
sources:
  - "[[Clippings/articles/Obsidian Cli 基础使用教程 AI化知识管理全过程]]"
  - "[[Clippings/articles/Obsidian x Agent 终极指南，从零打造个人 Agent 系统]]"
tags:
  - Obsidian
  - Claude Code
  - CLI配置
status: stable
---

# Obsidian CLI 配置指南

> Obsidian v1.12 官方 CLI + Claude Code 配置指南，让 AI 直接进入仓库操作。

## 前置条件

- Obsidian v1.12 或更高版本
- Node.js 18+ 或 Bun
- Claude Code（或其他 Coding Agent）

## Step 1：开启 Obsidian CLI

Obsidian 设置 → 通用 → 命令行界面 → 注册

系统自动将 `obsidian` 命令注册到 PATH。

验证：
```bash
obsidian --version
```

## Step 2：安装 Claude Code

```bash
# npm
npm install -g @anthropic-ai/claude-code

# 国内镜像
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```

验证：
```bash
claude --version
```

## Step 3：配置模型（国内可用）

### MiniMax Coding Plan

推荐方案：MiniMax Coding Plan ¥29/月起

购买地址：https://platform.minimaxi.com/subscribe/coding-plan

### 配置 settings.json

```bash
mkdir -p ~/.claude && touch ~/.claude/settings.json
```

内容：
```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.minimaxi.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "你的Key",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_MODEL": "MiniMax-M2.5",
    "ANTHROPIC_SMALL_FAST_MODEL": "MiniMax-M2.5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M2.5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M2.5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M2.5"
  }
}
```

### 配置 .claude.json

```bash
touch ~/.claude.json
```

内容：
```json
{
  "hasCompletedOnboarding": true
}
```

## Obsidian URI Scheme

CLI 注册后可通过 URI 直接操作：

| 操作 | URI |
|-----|-----|
| 新建文件 | `obsidian://new?vault=Vault名&name=文件名&content=内容` |
| 打开文件 | `obsidian://open?vault=Vault名&file=路径/文件名` |
| 搜索 | `obsidian://search?vault=Vault名&query=关键词` |

## 用 Claude Code 操作 Obsidian

```bash
# 进入 Vault 目录
cd ~/Documents/GitHub/obsidian

# 启动 Claude Code
claude

# 示例命令
"帮我在仓库里建一套知识管理的文件夹结构"
"批量给没有标签的笔记打上标签"
"读取 CLAUDE.md，然后帮我整理收件箱"
```

## 核心能力

| 能力 | 说明 |
|-----|------|
| 快速建立结构 | 一句话生成文件夹和模板文件 |
| 批量整理旧笔记 | AI 直接在仓库操作，真正批量 |
| 指令复用 | 常用操作存成指令反复调用 |

## 相关页面

- [[Obsidian]] - CLI 是 Obsidian 的 AI 通道
- [[主流模型汇总]] - MiniMax Coding Plan 详情
- [[工具模型配置汇总]] - 各工具配置方法汇总

## 来源

- [[Clippings/articles/Obsidian Cli 基础使用教程 AI化知识管理全过程]] - ShikiLab，2026-03-18
- [[Clippings/articles/Obsidian x Agent 终极指南，从零打造个人 Agent 系统]] - 空格丶，2026-04-22