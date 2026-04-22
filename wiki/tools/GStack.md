---
title: GStack
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]"
tags:
  - tool
  - agent
  - skill
  - coding
status: stable
---

# GStack

> YC总裁Garry Tan开源的AI编码Skill工作流，7万+Star，每天3万开发者使用

## 工具概述

| 项目信息 | |
|---------|---------|
| **开发者** | Garry Tan（YC总裁） |
| **Star数** | 7万+ |
| **日活** | 3万开发者 |
| **定位** | AI写代码用的Skill工作流模板 |
| **协议** | MIT |

## 核心定位

GStack教Agent怎么写代码。是Claude Code圈子里最火的模板之一。

## 与GBrain的关系

| 项目 | 职责 | 类比 |
|-----|------|------|
| **GStack** | 编码执行 | "手" |
| **GBrain** | 记忆思考 | "脑" |

两者可独立使用，也能合体。GStack的编码Skill在动手前会先查GBrain，看之前是否讨论过、决定过什么。

## 设计哲学

遵循 **Thin Harness, Fat Skill** 设计理念：
- 把智能放在Skill里
- Runtime越薄越好
- Skill文件就是代码，是知识工作最强载体

## 安装与使用

配合Claude Code使用：

```bash
# 克隆仓库
git clone https://github.com/garrytan/gstack.git

# Claude Code加载Skill
# 将Skill文件放入.claude/目录
```

## 核心Skill

GStack包含多个编码相关Skill，覆盖：
- 项目结构理解
- 代码规范遵循
- 测试流程
- Git操作
- 文档生成

## 相关工具

- [[tools/GBrain]] - 长期记忆系统（配合使用）
- [[tools/Claude Code]] - 主要使用平台
- [[tools/Hermes Agent]] - 可接入使用

## 相关概念

- [[concepts/Skill]] - Skill设计理念
- [[concepts/Thin Harness Fat Skill]] - 设计哲学
- [[concepts/GBrain]] - 与GBrain配合关系

## 人物

- [[people/Garry Tan]] - 项目作者、YC总裁

## 来源

- [[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]
- GitHub: github.com/garrytan/gstack（隐含引用）