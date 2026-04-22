---
title: Claude Code
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Claude Code 国内丝滑部署指南.md]]"
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
  - "[[Clippings/articles/Claude Code 官方文档.md]]"
tags: [工具, AI编程, Anthropic, 终端]
status: stable
---

# Claude Code

> Anthropic 推出的终端 AI 编程助手，可直接在命令行与 AI 协作写代码

## 官方资源

| 资源 | 链接 |
|-----|------|
| **官方文档** | https://code.claude.com/docs/en/overview |
| **安装指南** | https://code.claude.com/docs/en/installation |
| **配置说明** | https://code.claude.com/docs/en/configuration |
| **GitHub** | https://github.com/anthropics/claude-code |

## 核心特性

- **终端集成**：在命令行直接使用，适合习惯 Git、编辑器的开发者
- **项目理解**：能读取项目文件，理解代码结构
- **多平台支持**：Windows (WSL/Git Bash)、macOS、Linux
- **原生安装**：自包含可执行文件，不依赖 Node.js
- **MCP集成**：扩展工具能力
- **Skills系统**：自定义工作流

## 安装方式

### 方式一：原生安装（推荐）

```bash
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Homebrew (macOS)
brew install --cask claude-code
```

### 方式二：npm安装（需Node.js 18+）

```bash
npm install -g @anthropic-ai/claude-code
```

### Windows 详细步骤

1. **安装WSL**（推荐）：
   ```powershell
   wsl --install
   ```

2. **或使用Git Bash**：
   - 安装 Git for Windows
   - 在 Git Bash 中运行安装命令

3. **PowerShell直接安装**：
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```

4. **验证安装**：
   ```bash
   claude --version
   ```

## 配置要点

### 配置文件位置

| 系统 | 路径 |
|-----|------|
| **Windows** | `C:\Users\用户名\.claude\settings.json` |
| **macOS/Linux** | `~/.claude/settings.json` |

### 配置格式

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-你的API令牌",
    "ANTHROPIC_BASE_URL": "https://api.anthropic.com",
    "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929",
    "ANTHROPIC_SMALL_FAST_MODEL": "claude-haiku-4-5-20251001"
  }
}
```

### 配置项说明

| 配置项 | 说明 |
|-------|------|
| `ANTHROPIC_AUTH_TOKEN` | API认证令牌，以`sk-`开头 |
| `ANTHROPIC_BASE_URL` | API服务地址（官方或中转） |
| `ANTHROPIC_MODEL` | 主模型ID |
| `ANTHROPIC_SMALL_FAST_MODEL` | 快速小模型ID |

### 第三方中转配置

国内用户可通过中转服务访问：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-中转密钥",
    "ANTHROPIC_BASE_URL": "https://中转服务地址",
    "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929"
  }
}
```

**中转服务推荐**：
- 使用 [[tools/cc-switch]] 一键切换
- 或手动配置 Base URL

## 常见问题

| 问题 | 解决方案 |
|-----|---------|
| 命令找不到 | 检查PATH环境变量，重启终端 |
| Invalid API Key | 检查配置文件路径和令牌格式 |
| offline状态 | 不影响使用，仅表示无法连接Google |
| fetch failed | 检查网络代理配置 |
| Windows安装失败 | 使用WSL或Git Bash |

## 常用命令

| 命令 | 作用 |
|-----|------|
| `claude` | 启动交互式对话 |
| `claude --version` | 查看版本 |
| `claude --help` | 查看帮助 |
| `claude config` | 配置管理 |
| `claude doctor` | 诊断问题 |

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
- [[tools/cc-switch]] - 一键切换国产模型
- [[tools/Claudian]] - Obsidian插件
- [[people/Karpathy]]

## 来源

- [[Clippings/articles/Claude Code 国内丝滑部署指南.md]]
- [[Clippings/articles/Obsidian + Claude Code 教程.md]]
- [[Clippings/articles/Claude Code 官方文档.md]]