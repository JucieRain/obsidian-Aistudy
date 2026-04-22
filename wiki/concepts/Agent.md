---
title: Agent
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Hermes Agent 新手教程.md]]"
  - "[[Clippings/articles/飞书云文档.md]]"
tags: [概念, AI, 自主执行]
status: stable
---

# Agent

> AI 代理，能自主执行任务的智能系统

## 核心特征

- **自主执行**：不只是回答，而是完成任务
- **工具调用**：能操作外部系统（飞书、代码库、数据库）
- **多轮规划**：分解复杂任务，逐步执行
- **上下文保持**：长对话中保持一致性

## Agent 的「手」

飞书 CLI 文档比喻：AI Agent 很聪明，但没有「手」：
- 看不到日历
- 读不了群聊
- 打不开文档

CLI/API 就是给 Agent 的「手」，让它能操作实际系统。

## 常见 Agent 类型

| 类型 | 代表 |
|-----|------|
| **编程 Agent** | Claude Code、Codex、Cursor |
| **知识 Agent** | Hermes Agent、OpenClaw |
| **工作流 Agent** | 飞书 CLI 接入的 Agent |

## Agent 接入飞书

两种身份：
- **用户身份**：Agent 代表用户操作
- **应用身份**：Agent 代表应用操作

需要处理：
- 用户白名单
- 私聊配对
- 权限配置

## 参见

- [[tools/Hermes Agent]]
- [[tools/Claude Code]]
- [[tools/飞书]]

## 来源

- [[Clippings/articles/Hermes Agent 新手教程.md]]
- [[Clippings/articles/飞书云文档.md]]