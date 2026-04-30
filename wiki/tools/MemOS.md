---
title: MemOS
created: 2026-04-30
updated: 2026-04-30
sources:
  - "[[Clippings/articles/给 10 万 Star 的 Hermes 装个记忆外挂，AI 终于能越用越聪明了]]"
tags:
  - Agent
  - 记忆系统
  - Hermes
status: stable
---

# MemOS

> 记忆张量 MemTensor 团队开源的 AI 记忆系统，GitHub 8400+ Star，为 Hermes Agent 提供智能记忆插件。

## 核心定义

MemOS 是一个本地记忆系统，为 AI Agent 提供智能记忆管理能力：记忆存得聪明、记忆找得准。

## 核心能力

### 写入机制

语义分片 → LLM摘要 → 向量化 → 智能去重

**智能去重**是最有价值的部分：
- 不是简单文本比对
- 让 LLM 判断是重复、需要更新、还是全新
- 自动识别更新并合并，记录合并历史

### 检索机制

混合检索引擎：全文搜索 + 向量语义搜索

流程：融合排序 → 多样性去重 → 时间衰减 → 相关性过滤

### 预检索注入

每轮对话开始时，系统自动用最新消息做预检索，把相关记忆注入上下文。如果没命中，还会提示 Agent 自己去主动搜索。

## 与 Hermes 原生对比

| 对比维度 | Hermes 原生 MEMORY | MemOS 插件 |
|---------|-------------------|-----------|
| 写入机制 | Hermes认为重要才写入 | 自动提取实体、事实、关系 |
| 容量上限 | ≈2200字符硬上限 | 无硬上限 |
| 知识组织 | 线性文本 | 知识图谱 |
| 检索方式 | SQLite文本匹配 | 混合检索引擎 |

## 技能生成增强

支持三级独立模型配置：
- Embedding：轻量模型
- 摘要：中等模型
- 技能生成：最强模型

加一层规则过滤 + LLM评估，只有可重复、有价值的任务才生成技能。

降级机制：技能模型挂了自动降到摘要模型，再挂降到 Hermes 原生模型。

## 多 Agent 协同

两层协同能力：
- **同一机器**：多Agent独立记忆空间，可共享公共记忆和技能
- **跨机器**：Hub-Client架构，私有数据留本地，只有明确共享内容对团队可见

## 安装方式

```bash
curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/openclaw-local-plugin-20260408/apps/memos-local-plugin/install.sh | bash
```

安装后自动检测环境、安装依赖、创建软链接、更新配置、启动守护进程。

管理面板地址：http://127.0.0.1:18901

## 相关工具

- [[Hermes Agent]] - MemOS 为 Hermes 提供记忆插件
- [[长期记忆]] - MemOS 是长期记忆的具体实现

## 来源

- [[Clippings/articles/给 10 万 Star 的 Hermes 装个记忆外挂，AI 终于能越用越聪明了]] - 逛逛，2026-04-23
- GitHub: https://github.com/MemTensor/MemOS