---
title: GBrain
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]"
tags:
  - concept
  - agent
  - memory
status: stable
---

# GBrain

> YC总裁Garry Tan开源的AI Agent长期记忆系统，解决Agent"金鱼脑"问题

## 核心定义

GBrain是给AI Agent用的**长期记忆系统**。Agent接入后，会在用户睡觉时自己变聪明——自动消化会议记录、邮件、推特、语音通话、想法，补全人物资料、修复坏链、整理记忆。

开源十几天获得 **9K+ Star**，作者本人用它跑真实Agent：17888个页面、4383个人物、723家公司、21个定时任务全自动运转。

## 与 GStack 的关系

| 项目 | 职责 | 定位 |
|-----|------|------|
| **GStack** | 教Agent怎么写代码 | "手"（执行层） |
| **GBrain** | 教Agent怎么记事和思考 | "脑"（记忆层） |

两个项目可独立使用，也能合体。`hosts/gbrain.ts` 是连接桥——GStack编码Skill在动手前会先查脑子，看之前是否讨论过、决定过什么。

## 核心设计哲学

### Thin Harness, Fat Skill

把智能放在Skill里，Runtime越薄越好。Garry Tan："Skill文件就是代码，是目前做知识工作最强的载体。"

### Compiled Truth + Timeline 知识模型

每个brain page分两层：

| 层级 | 内容 | 特性 |
|-----|------|------|
| **Compiled Truth** | 当前最佳理解 | 可随时改写 |
| **Timeline** | 原始证据记录 | 只追加不删除 |

设计初衷：让认知能进化，又不丢历史。覆盖式更新+纯追加的两边好处都拿了。

## 4个核心亮点

### 1. 25个Skill即插即用

**永远在线的两个Skill：**

| Skill | 作用 |
|-------|------|
| **signal-detector** | 每条消息进来后台跑小模型，抓观点和人物 |
| **brain-ops** | 回答前先查脑，查不到就告诉你，不瞎编 |

**其他Skill分类：**
- 内容摄入类：会议、邮件、推特、PDF、视频、GitHub仓库
- 运维类：cron调度、每日简报、引用自检、过期页面巡检

### 2. 混合搜索 + 实体自动升级

**搜索策略：**
- 向量搜索 + 关键词搜索 + RRF融合 + 多查询扩展 + 4层去重
- 关键词精准命中原话，向量找意思相近内容

**实体自动升级机制：**

| 提及次数 | 自动操作 |
|---------|---------|
| 1次 | 生成stub页面 |
| 3次+ | 自动联网补料（LinkedIn、Twitter、公司主页） |
| 8次+ 或开过会 | 完整管线生成详细dossier |

**fail-improve循环：** 每次LLM兜底分类都被记录，系统自动生成更好的正则。意图分类器从第一周40%确定性涨到87%。

### 3. 能打电话的脑子

集成 Twilio + OpenAI Realtime。打电话进去，AI接起来时已从脑子拉出全部上下文：
- 上次聊了什么
- 合作过的项目
- 未结的话题

通话结束自动生成brain page：完整转录、自动识别实体、交叉引用。

### 4. 自进化能力

脑子自己在变得更便宜更准。无需手动标注谁重要——系统自动从交互频率判断。

## 部署方式

### 路线A：让Agent自己装

```ruby
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

Agent自己克隆仓库、装GBrain、建脑子、加载25个Skill、配定时任务。约30分钟。

### 路线B：本地CLI

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain
bun install && bun link
gbrain init       # 本地脑子，2秒拉起
gbrain import ~/notes/  # 导入笔记
gbrain query "我的笔记里反复出现的主题是什么?"
```

默认用PGLite（嵌入式Postgres），零配置。超过1000文件可迁到Supabase。

### 路线C：接入Claude Code/Cursor

```json
{
  "mcpServers": {
    "gbrain": { "command": "gbrain", "args": ["serve"] }
  }
}
```

30+ MCP工具通过stdio暴露，Claude写代码时可直接读脑子内容。

## 相关概念

- [[concepts/Agent]]
- [[concepts/长期记忆]]
- [[concepts/Skill]]

## 参见

- [[tools/GStack]] - Garry Tan的编码Skill工作流
- [[tools/GBrain]] - 工具页面（安装与配置）
- [[people/Garry Tan]] - YC总裁、项目作者
- [[tools/Hermes Agent]] - 可接入GBrain的Agent框架

## 来源

- [[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]
- GitHub: github.com/garrytan/gbrain