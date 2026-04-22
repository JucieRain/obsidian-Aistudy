# Wiki 知识库索引

> 最后更新：2026-04-22 | 总页面数：16
> 知识库主题：AI 落地实践研究

---

## 概念 Concepts

> AI 领域核心概念与理论

| 页面 | 摘要 | 来源数 |
|-----|------|-------|
| [[concepts/LLM Wiki]] | Karpathy 方法：用 LLM 增量构建和维护持久化 Wiki | 2 |
| [[concepts/第二大脑]] | 个人知识管理系统，传统问题与 LLM Wiki 解决方案 | 1 |
| [[concepts/Agent]] | AI 代理，自主执行任务的智能系统 | 2 |

---

## 工具 Tools

> AI 相关工具、产品、平台

| 页面 | 摘要 | 来源数 |
|-----|------|-------|
| [[tools/Claude Code]] | Anthropic 终端 AI 编程助手，LLM Wiki 核心工具 | 2 |
| [[tools/Obsidian]] | Markdown 知识管理工具，双向链接与图谱视图 | 1 |
| [[tools/Hermes Agent]] | Nous Research 开源 AI Agent，支持飞书接入 | 2 |
| [[tools/飞书]] | 字节跳动企业协作平台，AI Agent 接入能力 | 2 |
| [[tools/OpenClaw]] | 阿里云 AI Agent 服务，飞书集成 | 1 |
| [[tools/OpenClaw 系列文档]] | OpenClaw PDF 文档集索引 | 3 |
| [[tools/Claudian]] | Claude Code 嵌入 Obsidian 的插件 | 1 |
| [[tools/cc-switch]] | Claude Code 配置管理桌面应用 | 1 |
| [[tools/Obsidian Skills]] | 教 Claude 操作 Obsidian 的技能包 | 1 |
| [[tools/Web Clipper]] | Obsidian 网页剪藏插件 | 2 |
| [[tools/主流模型汇总]] | 2026年4月主流 AI 模型定价与订阅指南 | 官网 |

---

## 人物 People

> AI 领域关键人物

| 页面 | 摘要 | 来源数 |
|-----|------|-------|
| [[people/Karpathy]] | OpenAI 创始团队、前 Tesla AI 总监，LLM Wiki 方法提出者 | 2 |

---

## 趋势 Trends

> AI 发展趋势分析

| 页面 | 摘要 | 来源数 |
|-----|------|-------|
| （待录入） | | |

---

## 实践 Practices

> 团队赋能内容与实施指南

| 页面 | 摘要 | 来源数 |
|-----|------|-------|
| [[practices/Obsidian Git 同步]] | Git 实现 Obsidian 跨设备同步方案 | 1 |
| [[practices/今日待办]] | 2026-04-22 AI 学习与知识整理待办清单 | - |

---

## 综合 Synthesis

> 跨主题综合分析

| 页面 | 摘要 | 来源数 |
|-----|------|-------|
| [[synthesis/AI 信息源推荐]] | AI 领域信息源汇总：Twitter、公众号、网站、博客 | 1 |

---

## 统计

- **素材总数**：10 文章 + 3 PDF
- **已处理素材**：10/13 篇 (77%)
- **Wiki 页面数**：18
- **概念页面**：3
- **工具页面**：10
- **人物页面**：1
- **实践页面**：2
- **综合页面**：1

---

## 知识结构图

```
┌─────────────────────────────────────────────────────┐
│                    LLM Wiki 方法                     │
│                        (Karpathy)                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│   Claude Code ─────► Obsidian ─────► Web Clipper   │
│        │                │                           │
│        ▼                ▼                           │
│   Claudian ◄────► Obsidian Skills                   │
│        │                                             │
│        ▼                                             │
│   cc-switch                                          │
│                                                     │
├─────────────────────────────────────────────────────┤
│                    Agent 生态                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│   Hermes Agent ─────► 飞书 ◄────► OpenClaw         │
│        │                │                           │
│        ▼                ▼                           │
│   (消息网关)        (飞书 CLI)                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

*本索引由 AI 自动维护，每次录入后自动更新*