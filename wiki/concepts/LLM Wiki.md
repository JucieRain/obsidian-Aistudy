---
title: LLM Wiki
created: 2026-04-22
updated: 2026-07-05
sources:
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
  - "[[Clippings/articles/llm Wiki 养了三周，开始出毛病了]]"
  - "[Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)"
  - "[[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]"
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

## 实践经验：三个毛病

三周实践后发现的问题（来源：AI赋能说）：

| 毛病 | 表现 | 根因 |
|-----|------|------|
| **漂移** | Wiki页面和原文不一致 | AI摘要是有损压缩，每次更新都可能引入偏差 |
| **孤岛** | 有些页面没人引用 | 没有主动关联机制 |
| **找不到** | AI忘记早期内容 | Wiki超过50页，index.md太长，效率下降 |

详见 [[concepts/知识漂移]]

## 实践经验：三个解法

| 解法 | 内容 |
|-----|------|
| **溯源** | 每个关键事实标注来源行号（不是文件名） |
| **体检** | 定期检查矛盾/过时/孤岛/断链/漂移（每周常规+每月深度） |
| **搜索** | Wiki超过50页后需要搜索工具（[[tools/qmd]]） |

详见 [[practices/LLM Wiki维护经验]]

## 核心认知

- Human owns verification（人拥有验证权）
- AI是园丁，可以浇水除草
- 但种什么花、留哪棵——人说了算

## LLM Wiki v2 六大扩展 | 2026-07-05

> — [[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]

agentmemory 项目在 Karpathy 原版基础上的演进：

1. **置信度评分**：每个事实有分数，随时间衰减，被新来源确认时回升
2. **记忆四级层级**：工作记忆 → 情景记忆（摘要）→ 语义记忆（事实）→ 程序记忆（模式）
3. **遗忘曲线**：长期未访问的知识降噪处理，保留关键信息
4. **知识图谱**：类型化的实体与关系，支持影响分析
5. **混合搜索**：BM25 + 向量 + 图遍历，准确率 95.2%（LongMemEval-S）
6. **自动化钩子**：新源自动摄取、实体抽取、图谱更新、定期检查

> — [[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]], L240-260

## 参见

- [[people/Karpathy]]
- [[people/AI赋能说]] - 发现问题并提出解法
- [[concepts/第二大脑]]
- [[concepts/知识漂移]] - 漂移问题详解
- [[tools/qmd]] - 本地Markdown搜索引擎
- [[tools/Claude Code]]
- [[tools/Obsidian]]
- [[practices/LLM Wiki维护经验]]

## 来源

- [[Clippings/articles/Obsidian + Claude Code 教程.md]]
- [[Clippings/articles/llm Wiki 养了三周，开始出毛病了]]
- [Karpathy Gist 规则文档](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)