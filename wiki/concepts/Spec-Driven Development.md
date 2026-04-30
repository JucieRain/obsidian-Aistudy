---
title: Spec-Driven Development
created: 2026-04-30
updated: 2026-04-30
sources:
  - "[[Clippings/articles/组织级AI软件工程转型：不仅是新工具，更是新组织]]"
tags:
  - AI工程化
  - 开发方法论
  - Agent
status: stable
---

# Spec-Driven Development (SDD)

> 规约驱动开发，AI Agent 工程化时代的核心开发方法论。

## 核心定义

Spec-Driven Development 是一种开发方法论，先编写精确的规约（Spec），再让 Agent 根据规约生成代码。规约是机器可读的需求描述，Agent 可以精确执行。

## 与传统开发对比

| 对比维度 | 传统开发 | SDD |
|---------|---------|-----|
| 需求表达 | 自然语言文档 | 机器可读规约 |
| 代码生成 | 人工编写 | Agent根据规约生成 |
| Review重点 | 代码逐行检查 | 规约正确性验证 |
| 可追溯性 | 需求-代码对应模糊 | 规约-代码精确对应 |

## 推荐框架

**OpenSpec** - 声明式、可diff、可code review的规约框架

特点：
- 声明式语法，清晰表达意图
- 可以diff，追踪规约变更
- 可以code review，纳入现有流程
- 不锁定特定工具

## 核心价值

1. **消除歧义**：规约精确，Agent不会瞎猜
2. **可追溯**：规约和代码精确对应，方便审计
3. **可复用**：规约可以沉淀为组织资产
4. **降低幻觉**：Agent有精确约束，减少错误输出

## 实施要点

- 规约粒度要细到什么程度，需要团队实验确定
- 规约纳入版本管理，和代码一起演进
- SE写可执行spec，开发写agent测试用例

## 相关概念

- [[组织级AI转型]] - SDD是转型的核心方法论
- [[Agent]] - Agent需要精确规约才能可靠执行
- [[Harness Engineering]] - Agent工程化框架

## 来源

- [[Clippings/articles/组织级AI软件工程转型：不仅是新工具，更是新组织]] - FusionCID，知乎，2026-04-22