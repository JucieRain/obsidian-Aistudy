---
title: LLM Wiki
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
  - "[Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)"
tags: [概念, 知识管理, Karpathy, 方法论]
status: stable
---

# LLM Wiki

> Karpathy 提出的知识库维护方法论：用 LLM 增量构建和维护持久化的 Wiki

## 核心洞察

### 传统 RAG 的问题

```
每次查询 → 从原始文档检索 → 重新推导 → 无积累
```

- 信息不合成，每次重新发现
- 矛盾/交叉引用需每次发现
- 无「知识编译」过程

### LLM Wiki 的突破

```
录入素材 → 编译知识 → 持续维护 → 复利增长
```

- Wiki 是**持久化、复利的资产**
- 交叉引用已建立
- 矛盾已标注
- 维护成本转移给 AI

## 三层架构

```
┌─────────────────────────────────────┐
│  Schema (CLAUDE.md)                  │  ← 规则文档，配置 AI
├─────────────────────────────────────┤
│  Wiki (wiki/)                        │  ← AI 维护的知识库
│  ├── concepts/                       │
│  ├── tools/                          │
│  ├── people/                         │
│  ├── index.md                        │
│  └── log.md                          │
├─────────────────────────────────────┤
│  Raw Sources (Clippings/)            │  ← 原始素材，不可变
│  ├── articles/                       │
│  ├── papers/                         │
│  └── videos/                         │
└─────────────────────────────────────┘
```

## 三种核心操作

### 1. Ingest（录入）

```
读取素材 → 提取概念/工具/人物 → 更新 wiki 页面 → 更新 index → 记录 log
```

一篇文章可能影响 10-15 个 wiki 页面。

### 2. Query（查询）

```
读 index.md → 定位相关页面 → 深入阅读 → 综合回答 → 可存为新页面
```

分级查询，token 高效。

### 3. Lint（健康检查）

检查项目：
- 孤儿页面（无入链）
- 缺失页面（概念提及但无页面）
- 信息矛盾
- 过时信息
- 断链

## 为什么有效

> 人类放弃 Wiki 的原因：维护负担增长快于价值
> LLM Wiki：维护成本接近零，Wiki 保持健康

## 应用场景

| 场景 | 说明 |
|-----|------|
| 个人研究 | 深度追踪某领域，持续积累 |
| 团队知识库 | Slack/会议/文档 → Wiki，AI 维护 |
| 读书笔记 | 每章录入，自动建人物/主题页面 |
| 学习新领域 | 话题拆解，概念页面导航 |

## 参见

- [[people/Karpathy]]
- [[concepts/第二大脑]]
- [[tools/Claude Code]]
- [[tools/Obsidian]]

## 来源

- [[Clippings/articles/Obsidian + Claude Code 教程.md]]
- [Karpathy Gist 规则文档](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)