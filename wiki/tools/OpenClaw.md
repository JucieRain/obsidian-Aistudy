---
title: OpenClaw
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/OpenClaw集成飞书.md]]"
tags: [工具, AI助手, 阿里云]
status: stable
---

# OpenClaw

> 阿里云推出的 AI Agent 服务，支持飞书集成

## 核心特性

- **一键部署**：轻量应用服务器预装镜像
- **飞书集成**：官方飞书插件即将内置 CLI 能力
- **百炼 API**：支持 Coding Plan 和按量计费两种模式
- **WebUI**：提供 Web 操作界面

## 部署流程

### 购买配置

1. 购买轻量应用服务器（内存 ≥2GiB）
2. 选择 OpenClaw 应用镜像
3. 配置百炼 API Key

### 飞书接入

**扫码接入**（推荐）：
1. 控制台 → 应用详情 → 通道配置 → 飞书
2. 扫描二维码完成授权

**手动配置**：
1. 创建飞书应用
2. 配置权限（JSON 批量导入）
3. 设置事件订阅
4. 发布版本

## API Key 配置

两种类型：
- **Coding Plan**：固定月费，月度额度，超时不计费
- **按量计费**：标准百炼 API Key

支持模型：`qwen3.5-plus`、`kimi-k2.5`、`MiniMax-M2.5`、`glm-5` 等

## 配对流程

新版本（≥2026.3.13）无需配对码，扫码即可。
旧版本需：
1. 向机器人发消息获取配对码
2. 在 WebUI 执行：`openclaw pairing approve feishu 配对码`

## 参见

- [[tools/飞书]]
- [[tools/Hermes Agent]]

## 来源

- [[Clippings/articles/OpenClaw集成飞书.md]]
- [[Clippings/papers/OpenClaw 完全指南.pdf]]