---
title: OpenClaw
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/OpenClaw集成飞书.md]]"
  - "[[Clippings/articles/OpenClaw在飞书和Telegram上养了12个AI员工，它们还会自己开会.md]]"
tags: [工具, AI助手, 阿里云, 多Agent]
status: stable
---

# OpenClaw

> 阿里云推出的 AI Agent 服务，支持多 Agent 路由、飞书/Telegram 多平台集成

## 核心特性

- **一键部署**：轻量应用服务器预装镜像
- **多 Agent 路由**：每个 bot 绑定独立 Agent，真·独立人格
- **跨平台集成**：飞书、Telegram、QQ、企业微信、钉钉
- **Agent 通信**：agentToAgent 支持 Agent 间协作
- **百炼 API**：支持 Coding Plan 和按量计费两种模式
- **WebUI**：提供 Web 操作界面

## 部署流程

### 购买配置

1. 购买轻量应用服务器（内存 ≥2GiB）
2. 选择 OpenClaw 应用镜像
3. 配置百炼 API Key

### 飞书接入

**扫码接入**（推荐）：
1. 控制台 → 应用详情 → 通道配置 → 飞书
2. 扫描二维码完成授权

**手动配置**：
1. 创建飞书应用
2. 配置权限（JSON 批量导入）
3. 设置事件订阅
4. 发布版本

## API Key 配置

两种类型：
- **Coding Plan**：固定月费，月度额度，超时不计费
- **按量计费**：标准百炼 API Key

支持模型：`qwen3.5-plus`、`kimi-k2.5`、`MiniMax-M2.5`、`glm-5` 等

## 配对流程

新版本（≥2026.3.13）无需配对码，扫码即可。
旧版本需：
1. 向机器人发消息获取配对码
2. 在 WebUI 执行：`openclaw pairing approve feishu 配对码`

## 参见

- [[tools/飞书]]
- [[tools/Hermes Agent]]
- [[people/俊哥AI副业]] - 多 Agent 实践案例
- [[concepts/多Agent协同]]

## 来源

- [[Clippings/articles/OpenClaw集成飞书.md]]
- [[Clippings/articles/OpenClaw在飞书和Telegram上养了12个AI员工，它们还会自己开会.md]]
- [[Clippings/papers/OpenClaw 完全指南.pdf]]

---

## 多 Agent 配置（进阶）

### 设计理念

OpenClaw 支持真·独立人格多 Agent：
- 每个 Agent 有独立的 workspace（工作区）
- 每个 Agent 有自己的 SOUL.md（人设文件）
- 每个 Agent 有自己的 memory（记忆系统）
- 不是"一个 AI 套了多个壳"，而是真正独立的"人"

### Agent 阵容定义

```json
{
  "agents": {
    "list": [
      { "id": "main", "default": true, "name": "大总管", "workspace": "/root/.openclaw/workspace" },
      { "id": "dev", "name": "开发助理", "workspace": "/root/.openclaw/workspace-dev" },
      { "id": "content", "name": "内容助理", "workspace": "/root/.openclaw/workspace-content" },
      { "id": "ops", "name": "运营增长", "workspace": "/root/.openclaw/workspace-ops" },
      { "id": "law", "name": "法务助理", "workspace": "/root/.openclaw/workspace-law" },
      { "id": "finance", "name": "财务助理", "workspace": "/root/.openclaw/workspace-finance" }
    ]
  }
}
```

**重点**：workspace 一定要分开！每个 Agent 的代码笔记不会混在一起。

### 飞书多账户配置

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "accounts": {
        "main": { "appId": "cli_xxxx1", "appSecret": "你的secret1" },
        "dev": { "appId": "cli_xxxx2", "appSecret": "你的secret2" },
        "content": { "appId": "cli_xxxx3", "appSecret": "你的secret3" },
        "ops": { "appId": "cli_xxxx4", "appSecret": "你的secret4" },
        "law": { "appId": "cli_xxxx5", "appSecret": "你的secret5" },
        "finance": { "appId": "cli_xxxx6", "appSecret": "你的secret6" }
      }
    }
  }
}
```

### bindings 路由绑定

告诉 OpenClaw 哪个飞书 bot 的消息交给哪个 AI 处理：

```json
{
  "bindings": [
    { "agentId": "main", "match": { "channel": "feishu", "accountId": "main" } },
    { "agentId": "dev", "match": { "channel": "feishu", "accountId": "dev" } },
    { "agentId": "content", "match": { "channel": "feishu", "accountId": "content" } },
    { "agentId": "ops", "match": { "channel": "feishu", "accountId": "ops" } },
    { "agentId": "law", "match": { "channel": "feishu", "accountId": "law" } },
    { "agentId": "finance", "match": { "channel": "feishu", "accountId": "finance" } },
    { "agentId": "main", "match": { "channel": "telegram" } },
    { "agentId": "main", "match": { "channel": "qqbot" } },
    { "agentId": "main", "match": { "channel": "wecom" } }
  ]
}
```

飞书的每个 accountId 绑一个 agent，Telegram、QQ、企微默认走大总管。

### agentToAgent 通信

让 Agent 能互相协作：

```json
{
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["main", "dev", "content", "ops", "law", "finance"]
    }
  }
}
```

### AGENTS.md 团队成员列表

每个 Agent 的 AGENTS.md 必须写明团队成员：

```markdown
## 🏢 团队成员
- **dev**（开发助理 💻）— 代码开发、技术架构、部署
- **content**（内容助理 ✍️）— 公众号文章、文案、内容创作
- **ops**（运营增长 📈）— 用户增长、社交媒体、市场推广
- **law**（法务助理 ⚖️）— 合同审查、合规咨询
- **finance**（财务助理 💰）— 成本核算、预算管理

需要协作时用 sessions_send 工具，agentId 填对应的 id。
```

### SOUL.md 人设文件

Agent 的灵魂文件：

```markdown
# SOUL.md - 开发助理

你是开发助理，专注于代码开发、技术架构和部署。

## 核心职责
- 写代码、调试、代码审查
- 技术方案设计和架构建议
- 部署和运维

## 风格
- 技术精准，回答简洁
- 直接给方案和代码，少说废话
```

### 踩坑经验

1. **旧版飞书插件不支持多账户** → 必须升级到内置新版
2. **AGENTS.md 不写团队成员** → Agent 不知道彼此存在，无法协作
3. **飞书应用需开启长连接事件订阅** → 否则 bot 无法接收消息

### 验证命令

```bash
openclaw agents list --bindings    # 查看所有 agent 和路由规则
openclaw channels status --probe   # 查看所有通道在线状态
```

看到 `Feishu xxx: running ✅` 就成功了。