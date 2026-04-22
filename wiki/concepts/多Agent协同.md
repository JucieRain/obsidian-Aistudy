---
title: 多Agent协同
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md]]"
tags:
  - concept
  - agent
  - collaboration
status: stable
---

# 多Agent协同

> 多个AI Agent分工合作完成任务，角色隔离+共享上下文+任务委派

## 核心定义

多Agent协同不是开几个进程互相调用，本质是：**角色隔离 + 共享上下文 + 任务委派**。

```
角色化分工（Profiles）
    + 共享上下文（Honcho）
    + 明确任务交接（Gateway + 共享记忆）
    = 多Agent协同系统
```

## 四个核心组件

| 组件 | 职责 | 类比 |
|-----|------|------|
| **Profiles** | 多个独立Agent的组织方式 | 公司里的不同部门 |
| **Gateway** | Agent对外收发消息的通道 | 公司的前台/客服 |
| **Honcho** | 多Agent共享长期记忆和上下文 | 公司的共享知识库 |
| **tmux** | 进程保活工具（非通信机制） | 让办公室的灯一直开着 |

## Agent间任务交接流程

1. **写入共享上下文**：总管将需求和调研报告写入用户workspace
2. **发送通知**：总管通过飞书@产品总监，触发gateway接收消息
3. **目标Agent读取**：产品总监从Honcho读取调研报告，开始输出PRD
4. **回写结果**：产品总监将PRD写入共享workspace，通过gateway通知总管

## 研发军团架构示例

完整的研发Agent军团：

```
profiles/
├── commander/          # 总管：调度、催办、汇总、推进
├── market-director/    # 市场总监：市场调研
├── product-director/   # 产品总监：PRD输出
├── architect-director/ # 架构总监：技术架构设计、PRD审核
├── dev-director/       # 开发总监：代码实现、Claude Code调用
└── test-director/      # 测试总监：测试验收、报告输出
```

## 完整工作流程

以"竞品价格监控看板"为例：

| 阶段 | 执行Agent | 任务内容 |
|-----|----------|---------|
| **市场调研** | market-director | 调研竞品、市场现状，报告发总管+私发用户 |
| **产品设计** | product-director | 基于调研输出PRD |
| **架构设计** | architect-director | 审核PRD可实现性，可打回修改 |
| **开发实现** | dev-director | 通过tmux控制Claude Code开发，自主规划执行 |
| **测试验收** | test-director | 全面测试输出报告，总管派发给dev修复 |

关键点：开发总监自主调用本地Claude Code，自行决策，7×24小时写代码。

## 模型能力要求

多Agent系统对模型的要求极高：
- **长任务稳定性**：几十轮对话不掉链
- **超长上下文不失忆**：精准引用前步输出
- **跨轮次任务链路保持**：任务链路完整不断

Kimi K2.6-code-preview 在这方面的表现：
- 任务目标识别准确（模糊需求→清晰步骤）
- 工具调用稳定（文件操作、搜索、终端命令无幻觉）
- 长上下文不失忆（数十轮后精准引用）

## Hermes Agent实现

### 创建多个Profile

```bash
hermes profile create commander
hermes profile create market-director
hermes profile create product-director
hermes profile create architect-director
hermes profile create dev-director
hermes profile create test-director
```

每个profile需要：
1. 设置模型和API Key
2. 定义角色职责和工作范围
3. 配置可使用的技能和工具

### 定义总管职责

```
从现在开始，你是我的研发总管。你的职责是接收我的需求，
并按"市场调研 -> PRD -> 架构设计 -> 开发实现 -> 测试验收"的流程推进。
你不直接做专业产出，只负责调度、催办、汇总和推进。
```

### 配置Agent间通信

通过Honcho实现：
- 总管写入共享上下文
- Gateway发送通知触发下游Agent
- 下游Agent从Honcho读取并执行
- 完成后回写结果并通知

## 核心原理

| 要素 | 说明 |
|-----|------|
| **角色隔离** | 每个Agent独立workspace，上下文不污染 |
| **共享记忆** | Honcho提供跨Agent知识库 |
| **任务交接** | Gateway触发+共享workspace读写 |
| **自主决策** | 开发Agent可自主调用Claude Code |

## 相关概念

- [[concepts/Agent]] - Agent基础概念
- [[concepts/长期记忆]] - Agent记忆系统
- [[concepts/Honcho]] - Hermes共享记忆组件

## 参见

- [[tools/Hermes Agent]] - 实现框架
- [[tools/飞书]] - 消息渠道
- [[tools/Claude Code]] - 开发Agent可调用

## 来源

- [[Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md]]
- 作者：苍何