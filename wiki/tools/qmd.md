---
title: qmd
created: 2026-04-30
updated: 2026-04-30
sources:
  - "[[Clippings/articles/llm Wiki 养了三周，开始出毛病了]]"
tags:
  - 搜索引擎
  - LLM Wiki
  - 本地工具
status: stable
---

# qmd

> 本地 Markdown 搜索引擎，BM25 + 向量混合搜索，全部在本地运行。

## 核心定义

qmd 是一个本地 Markdown 搜索引擎，为 LLM Wiki 提供检索能力。当 Wiki 超过 50 页后，index.md 占用过多 token，需要搜索工具帮助 AI 找到相关页面。

## 核心特点

- **混合搜索**：BM25（关键词）+ 向量语义搜索
- **本地运行**：全部在本地，数据不上传
- **双模式**：CLI 和 MCP Server 两种调用方式
- **Agent 可调用**：MCP 模式下 AI Agent 可以直接调用

## 为什么需要

LLM Wiki 超过 50 页后：
- index.md 占用大量 token
- AI 在里面"找东西"效率下降
- AI 开始"忘记"早期知识（不是真的忘了，是找不到了）

## 替代方案

如果不想装额外工具，简单的 grep 脚本也够用：

```bash
grep -ril "$1" ~/my-wiki/wiki/ | head -20
```

## 使用场景

当 AI 需要回答问题时，不再从 index.md 里"猜"哪些页面相关，而是从检索层里"查"到相关页面，然后只在这些页面上做推理。

## 相关概念

- [[LLM Wiki]] - qmd 是 LLM Wiki 的推荐搜索工具
- [[知识漂移]] - 搜索能力有助于发现漂移问题

## 来源

- [[Clippings/articles/llm Wiki 养了三周，开始出毛病了]] - AI赋能说，2026-04-22
- GitHub: https://github.com/tobi/qmd