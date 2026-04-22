---
title: cc-switch
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/一定要用 Claude 管理 Obsidian.md]]"
  - "[[Clippings/articles/cc-switch GitHub 项目.md]]"
tags: [工具, Claude配置, 开源]
status: stable
---

# cc-switch

> 跨平台桌面应用，一键切换 Claude Code 模型和API配置

## 项目信息

| 信息 | |
|-----|---------|
| **开发者** | farion1231 |
| **GitHub** | https://github.com/farion1231/cc-switch |
| **定位** | All-in-One配置管理工具 |
| **支持平台** | Windows / macOS / Linux |

## 核心功能

> A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

| 功能 | 说明 |
|-----|------|
| **一键切换模型** | 官方API → 第三方中转 → 国产模型 |
| **多工具支持** | Claude Code、Codex、OpenCode、OpenClaw、Gemini CLI |
| **MCP管理** | 可视化管理MCP服务器配置 |
| **Skills管理** | 自定义工作流配置 |
| **提示词管理** | 多套系统提示词 + 测试 |

## 支持的模型

### 国产兼容模型

- DeepSeek（便宜，能力强）
- Kimi（长上下文）
- GLM（智谱）
- MiniMax（多模态）
- 通义千问

### 第三方中转

支持配置第三方API中转服务，解决国内访问问题。

## 解决的问题

| 问题 | cc-switch解决方案 |
|-----|-----------------|
| 官方API价格贵 | 切换国产便宜模型 |
| 国内网络访问门槛 | 配置中转Base URL |
| 手动改配置麻烦 | GUI一键切换 |
| 多配置管理 | 可视化界面 |

## 安装方式

从 GitHub Releases 下载对应平台安装包：
- Windows: .exe
- macOS: .dmg
- Linux: .deb / .rpm

## 配置流程

1. 打开 cc-switch
2. 添加API配置（密钥 + Base URL）
3. 选择目标模型
4. 点击切换
5. Claude Code 自动使用新配置

## 使用场景

### 场景一：国内API访问

国内用户无法直接访问Anthropic API：
- 配置中转服务密钥
- 设置中转Base URL
- 一键切换，无需改settings.json

### 场景二：国产模型替代

- DeepSeek：便宜（¥2/百万tokens），能力强
- Kimi：超长上下文
- MiniMax：多模态支持

### 场景三：多配置管理

不同场景用不同模型：
- 开发调试用便宜模型
- 重要任务用旗舰模型
- 一键切换

## 与手动配置对比

| 方式 | 门槛 | 灵活性 |
|-----|-----|--------|
| **手动编辑settings.json** | 高 | 高 |
| **cc-switch GUI** | 低 | 中 |

## 参见

- [[tools/Claude Code]] - Claude Code配置详解
- [[tools/Claudian]] - Obsidian插件
- [[practices/工具模型配置汇总]] - 配置速查表

## 来源

- [[Clippings/articles/一定要用 Claude 管理 Obsidian.md]]
- [[Clippings/articles/cc-switch GitHub 项目.md]]