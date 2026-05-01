---
title: Mitchell Hashimoto
created: 2026-05-01
updated: 2026-05-01
sources:
  - "[[Clippings/papers/Hermes Agent 从入门到精通.pdf]]"
tags: [人物, HarnessEngineering, Terraform, HashiCorp]
status: stable
---

# Mitchell Hashimoto

> Harness Engineering 理念创始人——每次犯错就加一条规则，让 AI 永远不再犯同一个错

## 身份

- **Terraform 创造者**
- **HashiCorp 创始人**
- **Ghostty 终端模拟器开发者**

## 主要贡献

### Harness Engineering 命名

2026年初，Mitchell Hashimoto 第一个给「给 AI 造缰绳」这件事命名：**Harness Engineering**。

核心发现来自 LangChain 团队的实验：用同一个模型（GPT-5.2-Codex），只调整周围的「缰绳」配置，成绩从 52.8% 涨到 66.5%，排名从 Top 30 跳到 Top 5——**模型一行没改**。

结论：**瓶颈不是模型，是环境**。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §01

### Mitchell 的做法

Mitchell 用 Claude Code 时有个习惯：每次 Agent 犯错，就加一条规则到 CLAUDE.md。

典型规则：
- "不要在这个项目里用 any 类型。"
- "测试文件放在 __tests__ 目录下，不要放在 src 里。"
- "commit message 用英文，动词开头。"

一条一条加，几周下来，CLAUDE.md 变成了一份非常详细的项目规范。Agent 从一个什么都不知的新人，变成了解项目所有暗规则的老手。

Mitchell 说这感觉就像在训练一个新队员。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §03

### 手动 vs 自动对比

| 维度 | Mitchell 方式（手动） | Hermes 方式（自动） |
|-----|---------------------|-------------------|
| 规则来源 | 人观察到问题后手写 | Agent 自己从反馈中提炼 |
| 存储位置 | CLAUDE.md（单文件） | 多个 Skill 文件 + 记忆数据库 |
| 触发改进 | 人记得要加规则才会加 | 每次使用后自动评估 |
| 跨项目迁移 | 需要手动复制 CLAUDE.md | Skill 全局生效，所有项目共享 |
| 改进速度 | 取决于人的勤快程度 | 持续自动，不会懒 |

**关键洞察**：Mitchell 手动写的规则往往更精准，因为人类对自己的需求有更清晰的认知。但 Hermes 把门槛降到了零——不是每个人都有 Mitchell 那样的耐心去维护一份精细的规则文件。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §03

## 影响

Mitchell 的做法被 Hermes Agent 产品化：

- Hermes 的学习循环把 Mitchell 的「每次犯错加规则」自动化了
- 你不用亲自加规则，Agent 自己观察、总结、写入 Skill
-代价是你对规则的控制力会降低一些，但门槛降到了零

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §03

## 参见

- [[concepts/Harness Engineering]] — Mitchell 命名的理念
- [[concepts/学习循环]] — Mitchell 做法的自动化
- [[tools/Hermes Agent]] — Harness Engineering 的产品化
- [[tools/Claude Code]] — Mitchell 使用的工具

## 来源

- [[Clippings/papers/Hermes Agent 从入门到精通.pdf]] — §01 概念、§03 Mitchell做法