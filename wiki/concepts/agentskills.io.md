---
title: agentskills.io
created: 2026-05-01
updated: 2026-05-01
sources:
  - "[[Clippings/papers/Hermes Agent 从入门到精通.pdf]]"
tags: [概念, Skill, 互通标准, 生态]
status: stable
---

# agentskills.io

> Skill 互通标准——一个 Skill 插到哪里都能跑

## 定义

agentskills.io 是 2026年初开始被多个 Agent 工具采用的 Skill 互通标准。它定义了 Skill 的通用格式，让不同 Agent 工具之间的 Skill 可以互相迁移。

**核心意义**：Skill 不再绑定某个特定工具，变成一种可移植的能力单元。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §05

## 支持的工具

目前已有 **30+ 个工具**支持 agentskills.io 标准：

| 工具 | 说明 |
|-----|------|
| Claude Code | Anthropic 官方交互式编码 Agent |
| Hermes Agent | Nous Research 自改进 Agent |
| Cursor | AI 编程编辑器 |
| GitHub Copilot | 代码补全助手 |
| Gemini CLI | Google 命令行 Agent |

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §05

## 与 App Store 的区别

| 对比 | App Store 模式 | agentskills.io 模式 |
|-----|---------------|--------------------|
| 生态结构 | 每个平台一套生态，开发者要适配多端 | 一个 Skill 插到哪里都能跑 |
| 迁移成本 | 切换平台需要重新开发 | 直接复制使用 |
| 标准 | 各平台私有标准 | 通用开放标准 |

agentskills.io 更像 USB 接口——一个标准，所有设备都能用。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §05

## Skill 格式

每个 Skill 是一个独立的 markdown 文件，包含：

| 部分 | 作用 | 必须？ |
|-----|------|-------|
| **标题** | 让 Agent 快速识别用途 | 是 |
| **触发条件** | 什么时候激活这个 Skill | 强烈建议 |
| **行为规则** | 具体怎么做，步骤、约束、格式 | 是 |
| **示例** | 完整的输入→输出示例 | 强烈建议 |
| **不要做什么** | 明确边界，防止漂移 | 可选 |

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §10

## 实际迁移示例

从 Claude Code 迁移 Skill 到 Hermes：

**Claude Code Skill**（SKILL.md）：
```markdown
# 公众号文章审校
## 触发条件
当用户提到「审校」「降低AI味」「太AI了」「润色」时激活。
## 审校流程
### 第一遍：事实审校
- 检查所有数据、时间、产品名是否准确
...
```

**迁移方式**：直接复制到 `~/.hermes/skills/proofreading.md`，无需改格式、无需适配 API。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §10

## 长远影响

agentskills.io 的长远影响比任何单个工具本身都大：

1. **Skill 资产保值**：花在写 Skill 上的时间不会因为换工具而浪费
2. **生态互通**：OpenClaw 的 ClawHub 44000+ Skill 可被 Hermes 直接调用
3. **反向哺育**：Hermes 自动创建和改进的 Skill 也可以反哺回整个生态

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §16

## 与 OpenClaw ClawHub 的关系

| 维度 | OpenClaw ClawHub | Hermes Skill |
|-----|-----------------|--------------|
| 数量 | 44000+ | 40+ 预置 + Agent自创 + 社区 |
| 创建方式 | 人工编写 SOUL.md | Agent自主创建 + 人工编写 |
| 维护方式 | 人工更新 | 自动进化 + 人工干预 |
| 互通性 | agentskills.io 标准 | agentskills.io 标准（互通） |

如果 ClawHub 的 44000+ Skill 能通过 agentskills.io 被 Hermes 直接调用，Hermes 的能力边界瞬间就展开了。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §05, §16

## 参见

- [[concepts/Skill]] — Skill 的定义和机制
- [[tools/Hermes Agent]] — agentskills.io 支持方
- [[tools/Claude Code]] — agentskills.io 支持方
- [[tools/OpenClaw]] — ClawHub 44000+ Skill 库

## 来源

- [[Clippings/papers/Hermes Agent 从入门到精通.pdf]] — §05 Skill系统、§10 自定义Skill、§16 生态对比