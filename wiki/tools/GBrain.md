---
title: GBrain
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]"
tags:
  - tool
  - agent
  - memory
  - mcp
status: stable
---

# GBrain

> YC总裁Garry Tan开源的AI Agent长期记忆工具，7万+Star

## 工具概述

| 项目信息 | |
|---------|---------|
| **开发者** | Garry Tan（YC总裁） |
| **开源时间** | 2026年4月 |
| **Star数** | 9K+（十几天） |
| **协议** | MIT |
| **定位** | Agent长期记忆系统 |

## 安装方式

### 方式一：让Agent自装（推荐）

适用于已跑OpenClaw或Hermes Agent的用户：

```ruby
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

Agent会自动完成：克隆仓库→装GBrain→建脑子→加载25个Skill→配定时任务。

### 方式二：本地CLI体验

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain
bun install && bun link

# 初始化本地脑子（2秒）
gbrain init

# 导入现有笔记
gbrain import ~/notes/

# 查询脑子内容
gbrain query "我的笔记里反复出现的主题是什么?"
```

默认用PGLite（嵌入式Postgres），无需启服务、零配置。

### 方式三：MCP接入Claude Code/Cursor

配置 `settings.json`：

```json
{
  "mcpServers": {
    "gbrain": { "command": "gbrain", "args": ["serve"] }
  }
}
```

接完后，Claude Code写代码时可直接读脑子里的内容（架构决策讨论、人物偏好、会议结论）。

### 数据迁移

超过1000文件或多设备同步时，可迁移到Supabase：

```bash
gbrain migrate --to supabase
```

## 核心功能

### 25个内置Skill

| 类型 | Skill示例 |
|-----|----------|
| **永远在线** | signal-detector（抓观点人物）、brain-ops（查脑再答） |
| **内容摄入** | 会议、邮件、推特、PDF、视频、GitHub仓库 |
| **运维** | cron调度、每日简报、引用自检、过期巡检 |

### 知识模型

每个brain page两层结构：
- **Compiled Truth**：当前最佳理解（可改写）
- **Timeline**：原始证据（只追加）

### 实体自动升级

系统根据提及次数自动升级实体：
- 1次 → stub页面
- 3次+ → 联网补料
- 8次+ 或开过会 → 完整dossier

### 电话集成

Twilio + OpenAI Realtime 集成。通话时AI已拉出全部上下文，结束自动生成brain page。

## 实战数据

作者本人使用情况：
- **17888** 个页面
- **4383** 个人物
- **723** 家公司
- **21** 个定时任务
- 全自动运转，12天搭建完成

## 与GStack配合

GStack管"手"（编码），GBrain管"脑"（记忆）。`hosts/gbrain.ts`是连接桥：

```typescript
// GStack编码前先查GBrain
import { gbrain } from './hosts/gbrain.ts';
```

## 相关工具

- [[tools/GStack]] - 编码Skill工作流
- [[tools/Hermes Agent]] - 可接入GBrain的Agent框架
- [[tools/OpenClaw]] - 可接入GBrain的Agent框架
- [[tools/Claude Code]] - MCP方式接入

## 相关概念

- [[concepts/GBrain]] - 设计理念详解
- [[concepts/长期记忆]] - Agent记忆系统
- [[concepts/Thin Harness Fat Skill]] - 设计哲学

## 来源

- [[Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md]]
- GitHub: github.com/garrytan/gbrain