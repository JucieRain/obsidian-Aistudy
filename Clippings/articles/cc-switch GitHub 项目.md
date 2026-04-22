---
title: "cc-switch GitHub 项目"
source: "https://github.com/farion1231/cc-switch"
author:
  - "[[farion1231]]"
published:
created: 2026-04-22
description: "A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI"
tags:
  - "clippings"
  - "github"
---

# cc-switch GitHub 项目

> 跨平台桌面应用，一键切换 Claude Code 的模型和 API 配置

## 项目信息

| 信息 | |
|-----|---------|
| **开发者** | farion1231 |
| **GitHub** | https://github.com/farion1231/cc-switch |
| **定位** | Claude Code 配置管理工具 |
| **支持平台** | Windows / macOS / Linux |

## 核心功能

根据 GitHub 描述，cc-switch 是：

> A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

### 主要能力

| 功能 | 说明 |
|-----|------|
| **一键切换模型** | 官方API → 第三方中转 → 国产模型 |
| **多工具支持** | Claude Code、Codex、OpenCode、OpenClaw、Gemini CLI |
| **MCP管理** | 可视化管理 MCP 配置 |
| **Skills管理** | 自定义工作流配置 |
| **提示词管理** | 多套系统提示词 + 测试 |

### 支持的国产模型

- DeepSeek
- Kimi
- GLM
- MiniMax
- 通义千问

## 使用场景

### 场景一：国内API访问

国内用户无法直接访问 Anthropic API，需要通过中转服务。cc-switch 可以：
- 一键切换到中转 API
- 配置 Base URL 和密钥
- 无需手动编辑 settings.json

### 场景二：国产模型替代

想用国产模型替代 Claude：
- DeepSeek（便宜，能力强）
- Kimi（长上下文）
- MiniMax（多模态）

### 场景三：多配置管理

在不同场景使用不同模型：
- 开发调试用便宜模型
- 重要任务用旗舰模型
- 一键切换，无需改代码

## 安装方式

从 GitHub Releases 下载对应平台安装包：
- Windows: .exe
- macOS: .dmg
- Linux: .deb / .rpm

## 配置流程

1. 打开 cc-switch
2. 添加 API 配置（密钥 + Base URL）
3. 选择模型
4. 点击切换
5. Claude Code 自动使用新配置

## 与其他工具对比

| 工具 | 配置方式 | 门槛 |
|-----|---------|-----|
| **手动编辑** | 改 settings.json | 高 |
| **cc-switch** | GUI一键切换 | 低 |

## 参见

- [[wiki/tools/cc-switch]] - 工具详情页
- [[wiki/tools/Claude Code]] - Claude Code 配置方法
- [[wiki/practices/工具模型配置汇总]] - 配置速查表

## 来源

- https://github.com/farion1231/cc-switch