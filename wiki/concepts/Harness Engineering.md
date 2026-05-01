---
title: Harness Engineering
created: 2026-04-23
updated: 2026-05-01
sources:
  - "[[Clippings/articles/Harness Engineering：Agent开发的关键战场.md]]"
  - "[[Clippings/papers/Hermes Agent 从入门到精通.pdf]]"
tags: [概念, Agent工程化, AI开发范式, 缰绳工程, MitchellHashimoto]
status: stable
---

# Harness Engineering

> Agent 工程化框架，将大模型不确定性转化为可预测、可扩展、可维护的生产级系统
> — Clippings/articles/Harness Engineering：Agent开发的关键战场.md

## 命名由来

**Mitchell Hashimoto**（Terraform 的创造者）第一个给这件事命名。

2026年初，LangChain 团队做了一个实验：用同一个模型（GPT-5.2-Codex），只调整周围的「缰绳」配置，成绩从 52.8% 涨到 66.5%，排名从 Top 30 跳到 Top 5——**模型一行没改**。

核心发现：**瓶颈不是模型，是环境**。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §01

### Mitchell 的做法

Mitchell 用 Claude Code 时有个习惯：每次 Agent 犯错，就加一条规则，让它永远不再犯同一个错。

典型规则：
- "不要在这个项目里用 any 类型。"
- "测试文件放在 __tests__ 目录下，不要放在 src 里。"
- "commit message 用英文，动词开头。"

一条一条加，几周下来，CLAUDE.md 变成了一份非常详细的项目规范。Mitchell 说这感觉就像在训练一个新队员。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §03

## 定义

Harness Engineering（驾驭工程）是专门针对 AI Agent 的软件工程分支，研究如何通过系统化的工程方法，构建、部署、运行和维护可靠的 AI Agent 系统。

**核心使命**：为大模型这匹"野马"套上缰绳，让它在可控范围内发挥强大能力。

## 五组件模型与 Hermes 内建映射

| 组件 | 职责 | 手动实现方式 | Hermes Agent 内建系统 |
|-----|------|-------------|----------------------|
| **指令层** | 定义 Agent 行为规范 | 手写 CLAUDE.md / AGENTS.md | Skill 系统（自动创建 + 自改进） |
| **约束层** | 限制 Agent 能做什么 | 配置 hooks / linter / CI | Tool permissions + sandbox + toolset 按需启用 |
| **反馈层** | 让 Agent 知道做得好不好 | 人工审查 / 评估者 Agent | 自改进学习循环（完成任务后自动复盘优化） |
| **记忆层** | 让 Agent 跨会话保持知识 | 手动维护 knowledge base | 三层记忆（会话/持久/Skill）+ Honcho 用户建模 |
| **编排层** | 多 Agent 协调 | 自己搭多 Agent pipeline | 子 Agent 委派 + cron 调度 |

**关键区别**：手动方式全靠人，Hermes 把五组件全部内建，开箱即用。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §01

## 与传统软件工程的区别

| 维度 | 传统软件工程 | Harness Engineering |
|-----|------------|-------------------|
| 核心逻辑 | 确定性逻辑 | 概率性推理 |
| 输入输出映射 | 确定关系 | 概率性关系 |
| 测试方法 | 单元测试、集成测试 | 不完全适用，需智能纠错 |
| 错误处理 | 异常捕获 | 智能纠错和重试机制 |
| 可观测性 | 相对简单 | 极其复杂 |

## 三大核心价值

1. **可靠性**：通过智能编排、错误处理、自我反思等机制，降低幻觉率、卡壳率和跑偏率
2. **可扩展性**：支持从单任务到多任务、单Agent到多Agent的平滑演进
3. **可观测性**：实现Agent行为的可解释、可调试、可优化

## 六大核心战场

### 1. 智能编排与决策引擎

Agent 的"大脑"，决定如何思考、规划任务、做出决策。

**主流决策框架**：

| 框架 | 说明 |
|-----|------|
| ReAct | 思考-行动-观察循环，最基础最常用 |
| Plan-and-Execute | 先规划再执行，适合复杂多步骤任务 |
| Reflexion | 引入自我反思机制，提高学习和纠错能力 |

### 2. 工具集成与调用管理

Agent 连接现实世界的桥梁。

**关键技术**：
- 工具描述标准化（OpenAPI 格式）
- 工具调用上下文管理
- 工具链自动组合与优化

**常见问题**：工具滥用、调用失败、结果误解

### 3. 记忆系统工程

Agent 智能的基础。

**三层架构**：

| 层级 | 存储 | 用途 |
|-----|------|------|
| 短期记忆 | 内存 | 当前对话上下文 |
| 长期记忆 | 向量数据库 | 历史偏好、知识经验 |
| 工作记忆 | 工作台 | 当前任务相关信息 |

**关键技术**：向量检索、记忆摘要、记忆遗忘机制

### 4. 测试与评估体系

从原型走向生产的必经之路。

**测试维度**：
- 功能测试：任务完成率
- 鲁棒性测试：异常输入表现
- 安全性测试：有害内容检测
- 性能测试：响应时间、吞吐量

**评估方法**：自动化基准测试（MMLU、AgentBench）、人工评估、A/B测试

### 5. 监控与可观测性

生产级 Agent 的"眼睛"。

**三个层次**：
- 输入输出监控
- 中间步骤追踪
- 决策逻辑可视化

### 6. 安全与合规治理

Agent 落地的底线。

**关键技术**：
- 输入输出过滤
- 权限控制与沙箱
- 数据脱敏与隐私保护

## 业界标杆案例

### 编程辅助 Agent

| 产品 | Harness Engineering 创新 |
|-----|------------------------|
| Cursor | 智能代码索引系统、增量式上下文管理、多步骤生成验证 |
| Claude Code | 全项目一次性加载（1M上下文）、结构化思考过程展示 |
| GitHub Copilot | 边缘+云端混合推理、上下文感知提示工程、持续学习优化 |

### 通用 Agent 框架

| 框架 | 特点 |
|-----|------|
| LangGraph | 状态机概念、显式状态管理、循环分支支持、持久化断点续跑 |
| OpenAI Assistants API | 开箱即用、托管式服务、极低开发门槛 |

### 垂直领域 Agent

| 领域 | 案例 |
|-----|------|
| 法律 | Harvey AI：专业知识库、交叉验证、端到端加密 |
| 医疗 | IBM Watsonx Health：多模态处理、可解释决策、FDA/HIPAA合规 |

## 当前挑战与未来趋势

**主要挑战**：
- 标准化缺失
- 可解释性差
- 成本高昂（复杂Agent推理成本是Chatbot的几十倍）
- 人才短缺

**未来趋势**：
- 自动化 Harness：AI 辅助开发Agent
- 多Agent协同 Harness：Agent 社会
- 端云协同 Harness：边缘端降低延迟
- 行业专用 Harness：医疗、金融、法律定制化

## 参见

- [[concepts/Agent]]
- [[tools/Claude Code]]
- [[tools/Hermes Agent]] — 五组件的内建实现
- [[concepts/长期记忆]]
- [[concepts/多Agent协同]]
- [[concepts/学习循环]] — 反馈层的自动化
- [[people/Mitchell Hashimoto]] — Harness Engineering 理念创始人

## 来源

- [[Clippings/articles/Harness Engineering：Agent开发的关键战场.md]]
- [[Clippings/papers/Hermes Agent 从入门到精通.pdf]] — §01 概念、§03 Mitchell做法