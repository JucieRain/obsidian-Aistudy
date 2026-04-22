---
title: Hermes Agent
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Hermes Agent 新手教程.md]]"
  - "[[Clippings/articles/Hermes + 飞书踩坑修复.md]]"
tags: [工具, Agent, NousResearch, 飞书]
status: stable
---

# Hermes Agent

> Nous Research 推出的开源 AI Agent，支持多平台消息网关和多种 LLM Provider

## 核心特性

- **多模型支持**：OpenRouter、OpenAI、阿里云 DashScope 等
- **消息网关**：飞书、Discord 等平台接入
- **爬虫能力**：强大的网页内容抓取能力
- **上下文压缩**：长对话自动压缩保持上下文

## 安装流程

### 官方安装脚本

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes version
hermes doctor
```

### 常见依赖问题

```bash
# 补基础依赖
cd ~/hermes-agent
./venv/bin/python -m pip install pyyaml python-dotenv

# 最小可用安装（文本链路）
./venv/bin/python -m pip install -e ".[feishu]"
```

## 飞书接入要点

### 配置步骤

1. 获取飞书应用 App ID 和 App Secret
2. 配置 `DASHSCOPE_API_KEY` 或其他模型密钥
3. 设置用户白名单或放开所有用户：
   ```bash
   hermes config set GATEWAY_ALLOW_ALL_USERS true
   ```

### 常见问题

| 问题 | 原因 | 解决方案 |
|-----|------|---------|
| 网关运行但不回复 | 用户白名单拦截 | 配置 FEISHU_ALLOWED_USERS |
| 401 错误 | 模型路由错误 | 检查 model.provider 配置 |
| av/cython 构建失败 | 多媒体依赖可选 | 使用最小安装，后续再补 |

## 模型配置

### DashScope（阿里云通义）

```bash
hermes config set model.provider alibaba
hermes config set model.default qwen3.5-plus
hermes config set DASHSCOPE_API_KEY "你的密钥"
```

### OpenRouter

```bash
hermes config set OPENROUTER_API_KEY "sk-or-v1-xxx"
```

## 在知识库中的应用

- **素材收集**：爬取视频字幕、网页内容
- **跨设备同步**：通过 GitHub 同步到 Obsidian Vault
- **视频剪藏**：处理无字幕视频需要 Hermes 提取

## 参见

- [[tools/Claude Code]]
- [[tools/飞书]]
- [[concepts/Agent]]

## 来源

- [[Clippings/articles/Hermes Agent 新手教程.md]]
- [[Clippings/articles/Hermes + 飞书踩坑修复.md]]