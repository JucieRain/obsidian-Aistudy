---
title: Karpathy
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
  - "[Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)"
tags: [人物, OpenAI, Tesla, AI研究]
status: stable
---

# Karpathy

> Andrej Karpathy，OpenAI 创始团队成员、前 Tesla AI 总监，AI 领域知名研究者

## 背景

- **OpenAI**：创始团队成员，参与早期研究
- **Tesla**：前 AI 总监，负责 Autopilot 和 Full Self-Driving
- **教育**：斯坦福大学博士，深度学习课程 CS231n 作者

## LLM Wiki 方法

2026 年 4 月，Karpathy 发布了「LLM Knowledge Bases」方法：

### 核心理念

> **用 LLM 增量构建和维护持久化的 Wiki**

与传统 RAG 的区别：
- RAG：每次查询重新从原始文档检索，无积累
- LLM Wiki：知识被「编译」一次，持续维护，复利增长

### 三层架构

| 层级 | 内容 | 角色 |
|-----|------|------|
| Raw Sources | 原始素材 | 只读，来源 |
| Wiki | AI 维护的知识库 | AI 写，人读 |
| Schema | 规则文档 (CLAUDE.md) | 配置 AI 行为 |

### 三种操作

1. **Ingest**：录入素材，更新 wiki 页面
2. **Query**：查询知识，先读 index 再深入
3. **Lint**：健康检查，修复矛盾/孤儿页面

## 影响力

- 推文几天跑了几千万曝光
- 引发社区大量实践和讨论
- 成为「第二大脑」维护的新范式

## 参见

- [[concepts/LLM Wiki]]
- [[concepts/第二大脑]]
- [[tools/Claude Code]]
- [[tools/Obsidian]]

## 来源

- [[Clippings/articles/Obsidian + Claude Code 教程.md]]
- [Karpathy Gist 规则文档](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)