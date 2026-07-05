---
title: 女娲Skill
created: 2026-07-05
updated: 2026-07-05
sources: ["[[Clippings/articles/AI驱动的PPT工作流：女娲Skill+PPT Director.md]]"]
tags: [工具, Skill, Claude Code, Agent, AI工作流]
status: stable
---

# 女娲 Skill

> Claude Code 认知蒸馏工具：通过 6 Agent 并行调研，将具体人物或角色蒸馏为结构化认知模型

## 安装

```bash
npx skills add alchaincyf/nuwa-skill
```

## 核心能力

女娲的核心能力是**认知蒸馏**（见 [[concepts/认知蒸馏]]），将一个人的认知模式、决策偏好、表达习惯提炼为可被 AI 使用的 `.skill.md` 文件。

## 6 Agent 并行架构

| Agent | 职责 |
|-------|------|
| 著作 Agent | 调研著作、文章、公开讲话 |
| 对话 Agent | 分析对话风格、提问方式、思维习惯 |
| 表达 Agent | 提炼常用表达、比喻、价值判断方式 |
| 批评 Agent | 找出常见的否定模式、反感的事物 |
| 决策 Agent | 梳理决策框架、权重分配 |
| 时间线 Agent | 追踪认知演变和立场变化 |

## 使用方式

**情况 A**：知道具体是谁
```
用女娲蒸馏一个"袁家军"
```

**情况 B**：只知道角色类型
```
用女娲蒸馏一个"省级分管数字化的副省长"的认知模型
```

**情况 C**：有场景约束
```
用女娲蒸馏：
角色：某省分管数字化改革的副省长
场景：他在听一个区县的数字化改革成果汇报
他的决策模型是什么？关心什么？什么会让他认可？什么让他反感？
```

## 输出文件

| 文件 | 内容 |
|------|------|
| `audience-card.md` | 受众认知模型：心智模型、决策启发式、信息偏好、注意力分配 |
| `reviewer-card.md` | 评审认知模型：审查维度、合格标准、常见否决点、加分项 |

## 在 PPT 工作流中的角色

```
女娲（蒸馏受众+评审） → PPT Director（调度生产） → 达尔文（打磨优化）
```

> — [[Clippings/articles/AI驱动的PPT工作流：女娲Skill+PPT Director.md]]

## 参见

- [[concepts/认知蒸馏]]
- [[tools/PPT Director Skill]]
- [[tools/Claude Code]]
