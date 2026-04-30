---
title: Skill
created: 2026-04-30
updated: 2026-04-30
sources:
  - "[[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]"
tags:
  - Agent
  - 技能沉淀
  - 自进化
status: stable
---

# Skill

> Agent 自动沉淀的可复用能力单元，让做过的事情不需要再教一遍。

## 核心定义

Skill 是 Agent 在执行复杂任务时自动生成的可复用技能包。当 Agent 发现某个任务流程有价值且可重复时，会将其封装为 Skill，下次遇到类似任务可直接调用。

## 核心特点

| 特点 | 说明 |
|-----|------|
| **自动生成** | Agent 判断任务有复用价值后自动创建 |
| **可复用** | 下次遇到类似任务可直接调用，不需重新描述 |
| **可积累** | 用得越久，Skill 库越丰富 |
| **可共享** | 多 Agent 可共享 Skill 库 |

## Skill 生成条件

不是所有任务都会生成 Skill，需要满足：

| 条件 | 说明 |
|-----|------|
| **可重复** | 任务流程可以被标准化 |
| **有价值** | 执行结果对后续工作有帮助 |
| **复杂度适中** | 太简单不值得沉淀，太复杂难以标准化 |

## Skill 与记忆的区别

| 维度 | Skill | 记忆 |
|-----|-------|------|
| **内容** | 任务流程/操作方法 | 事实/偏好/上下文 |
| **形式** | 可执行的脚本/Prompt | 文本描述 |
| **触发** | Agent 主动判断生成 | 自动存储对话内容 |
| **复用** | 直接执行 | 作为参考信息 |

## Skill 分级体系（组织级）

| 级别 | 范围 | 说明 |
|-----|------|------|
| **L0** | 通用 | 跨项目、跨团队可用的基础 Skill |
| **L1** | 框架级 | 针对特定技术框架的 Skill |
| **L2** | 业务级 | 针对特定业务场景的 Skill |

## 代表性工具

| 工具 | 特点 |
|-----|------|
| [[tools/GStack]] | YC总裁Garry Tan开源，编码Skill工作流，7万+Star |
| [[tools/GBrain]] | 支持Skill自动生成和调用 |
| [[tools/Hermes Agent]] | `/skills` 命令查看积累的Skill |

## 使用示例

**Hermes Agent 中的 Skill**：

```bash
# 查看 Agent 积累的 Skill
/skills

# 输出示例
- skill: summarize-article
  uses: 23
  last_used: 2026-04-22

- skill: generate-prd
  uses: 12
  last_used: 2026-04-20
```

**自进化循环**：

```
执行任务 → 判断可复用 → 生成 Skill → 下次调用 → 优化 Skill → ...
```

## 相关概念

- [[Agent]] - Skill 是 Agent 的核心能力
- [[长期记忆]] - Skill 与记忆互补
- [[多Agent协同]] - 多 Agent 可共享 Skill
- [[GBrain]] - Skill 自动生成机制

## 相关工具

- [[tools/GStack]] - 编码 Skill 工作流
- [[tools/Hermes Agent]] - Skill 自动沉淀

## 来源

- [[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]] - Garry Tan, 2026-04
  > "GStack 是 Garry Tan 开源的编码 Skill 工作流" — L45-50