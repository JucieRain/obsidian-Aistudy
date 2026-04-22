---
title: 俊哥AI副业
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/OpenClaw在飞书和Telegram上养了12个AI员工，它们还会自己开会.md]]"
tags: [人物, 微信公众号, AI实践者, OpenClaw]
status: stable
---

# 俊哥AI副业

> 微信公众号博主，OpenClaw 多 Agent 深度实践者

## 身份

- **平台**：微信公众号「俊哥AI副业」「俊哥AI出海」
- **定位**：AI Agent 实践者、一个人公司（OPC）探索者
- **特点**：踩坑记录详尽、配置教程可复制

## 主要贡献

### OpenClaw 多 Agent 实践

在飞书和 Telegram 上部署 **12 个 AI 员工**：
- 6 个飞书 Agent：大总管小夏、开发助理、内容助理、运营增长、法务助理、财务助理
- 6 个 Telegram Agent：大总管小俊 + 5 个助理
- 实现 agentToAgent 通信，AI 员工可互相协作开会

### 关键技术分享

**多 Agent 路由配置**：
```json
{
  "agents": {
    "list": [
      { "id": "main", "name": "大总管小夏", "workspace": "/root/.openclaw/workspace" },
      { "id": "dev", "name": "开发助理", "workspace": "/root/.openclaw/workspace-dev" },
      // ...每个 Agent 独立 workspace
    ]
  }
}
```

**飞书多账户 bindings**：
```json
{
  "bindings": [
    { "agentId": "main", "match": { "channel": "feishu", "accountId": "main" } },
    { "agentId": "dev", "match": { "channel": "feishu", "accountId": "dev" } },
    // ...飞书 accountId 与 agentId 绑定
  ]
}
```

**踩坑经验**：
1. 旧版飞书插件不支持多账户，需升级新版
2. AGENTS.md 必须写明团队成员列表，否则 Agent 不知道彼此存在
3. 每个 Agent 的 SOUL.md 人设文件要精心设计

## 理念

### OPC（One Person Company）

一个人也可以是一家公司：
- 未来的公司可能不再需要 100 个人
- 未来的创业者一个人就是一支军队
- AI 不是工具，是同事、是团队

### 多 Agent vs 单一 AI

单一通用 AI 记不住整个公司的上下文，但多 Agent 各管一摊：
- 开发助理的 workspace 全是代码
- 财务助理的记忆全是账单和预算
- 各自深耕自己的领域，又能通过 agentToAgent 协作

## 其他骚操作

- 混合部署：云服务器跑 Gateway，Windows 本地跑 Node
- 手机远程打开 Windows 记事本
- 8 分钟部署两个宝宝起名网站

## 参见

- [[tools/OpenClaw]] - 多 Agent 路由配置来源
- [[concepts/多Agent协同]] - Agent 协作理念
- [[practices/OpenClaw养成路线图]] - 8 阶段养成教程

## 来源

- [[Clippings/articles/OpenClaw在飞书和Telegram上养了12个AI员工，它们还会自己开会.md]]