---
title: OpenClaw
created: 2026-04-22
updated: 2026-04-23
sources:
  - "[[Clippings/articles/OpenClaw集成飞书.md]]"
  - "[[Clippings/articles/OpenClaw在飞书和Telegram上养了12个AI员工，它们还会自己开会.md]]"
  - "[[Clippings/articles/Openclaw养龙虾秘籍大公开！【安全+省钱】.md]]"
  - "[[Clippings/papers/OpenClaw完全指南（花园版）.md]]"
  - "[[Clippings/papers/OpenClaw橙皮书-从入门到精通-v1.3.1.md]]"
  - "[[Clippings/papers/OpenClaw蓝皮书-1.0.0版.md]]"
tags: [工具, AI助手, 阿里云, 多Agent]
status: stable
---

# OpenClaw

> 开源、自托管的 AI Agent 平台，GitHub 历史增速第一（超越 React 和 Linux）

## 核心数据（截至 2026-03）

| 指标 | 数据 |
|-----|------|
| **GitHub Stars** | 超越 Linux（历史增速第一） |
| **Forks** | 53,232+ |
| **贡献者** | 1,075+ |
| **ClawHub Skills** | 13,700+ |
| **内置 Skills** | 55 个 |
| **支持消息渠道** | 20+ |

## 核心特性

- **一键部署**：轻量应用服务器预装镜像（阿里云/腾讯云/火山引擎等）
- **多 Agent 路由**：每个 bot 绑定独立 Agent，真·独立人格
- **跨平台集成**：飞书、Telegram、QQ、企业微信、钉钉、WhatsApp、Discord 等 20+ 平台
- **Agent 通信**：agentToAgent 支持 Agent 间协作
- **记忆系统**：四层记忆架构（SOUL/TOOLS/USER/Session），长期可持续
- **技能生态**：ClawHub 13,700+ Skills，Skills.sh 87,000+ 跨平台技能

## 部署流程

### 部署方式总览

| 平台 | 配置 | 价格 | 特点 |
|-----|------|------|------|
| **阿里云** | 2C2G | 9.9元/月 | 国内首选，镜像预装 |
| **腾讯云** | 2C4G | ~17元/月 | 企微/QQ 生态 |
| **火山引擎** | 2C4G | 9.9元/月 | 飞书深度集成 |
| **扣子编程** | 无需服务器 | ¥49/月起 | 零门槛，内置模型 |
| **本地 npm** | Node.js 22+ | 免费 | 开发者首选 |

### 本地安装命令

```bash
# 安装 OpenClaw
npm install -g openclaw@latest

# 初始化并安装守护进程
openclaw onboard --install-daemon

# 诊断检查
openclaw doctor
```

### 飞书接入

**扫码接入**（推荐）：
1. 控制台 → 应用详情 → 通道配置 → 飞书
2. 扫描二维码完成授权

**手动配置**：
1. 创建飞书应用
2. 配置权限（JSON 批量导入）
3. 设置事件订阅（推荐长连接模式）
4. 发布版本

---

## 记忆系统（核心特性）

### 四层记忆架构

OpenClaw 区别于普通 Chatbot 的核心能力是分层记忆：

| 层级 | 文件 | 作用 |
|-----|------|------|
| **身份层** | SOUL.md | 定义 AI 的性格、语调、行为边界（不可变内核） |
| **用户层** | USER.md | 用户的个人资料和偏好 |
| **操作层** | AGENTS.md | 操作指南、工作流程、能力边界 |
| **索引层** | MEMORY.md | 核心信息索引，保持精简（<40 行） |

### 日志系统

每日交互记录以 append-only 方式写入 `memory/YYYY-MM-DD.md` 文件。
Session 启动时自动读取今天和昨天的日志，提供连续性上下文。

### 向量记忆搜索

支持两种检索策略：
- **Embedding 向量**：语义搜索，模糊关联
- **BM25 关键词**：精确匹配，TF-IDF 加权

底层使用 SQLite-vec 进行向量存储和加速检索。

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
- [[Clippings/papers/OpenClaw完全指南（花园版）.md]] - 花园老师完整指南
- [[Clippings/papers/OpenClaw橙皮书-从入门到精通-v1.3.1.md]] - 花叔橙皮书
- [[Clippings/papers/OpenClaw蓝皮书-1.0.0版.md]] - 杨彧鑫AI蓝皮书

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

---

## 养龙虾省钱指南

### 为什么龙虾烧钱？

龙虾贵的原因：
- **上下文长**：每次对话要加载 SOUL/TOOLS/USER/MEMORY 等文件
- **记忆开销**：记住历史对话、任务进度、工具使用结果
- **工具元信息**：50+ 内置工具的描述一次性灌入上下文
- **模型成本**：好模型仍然贵，token 消耗是普通 Chatbot 的几十倍

### 省钱三大妙招

#### 1. 上下文瘦身

| 方法 | 操作 |
|-----|------|
| 瘦全身 | 定期筛查记忆和工具，删除过时信息 |
| 瘦肚子 | 禁用不常用内置工具，用 CLI 替代浏览器自动化 |
| 瘦大腿 | cron 替代心跳，不共享主会话上下文 |
| 瘦手臂 | `/compact` 压缩对话，隔离会话记忆 |

**筛查提示词**：
```
我们现在来一波没有用的工具筛查和过时记忆的筛查。
列出你所有每一次对话中加载的内容，找出哪些可以精简。
然后创建一个 cron 定时任务，每周一下午 2 点都做一遍这个操作。
```

#### 2. 模型混搭

不同难度任务配不同等级模型：

| 任务档位 | 推荐模型 | 适用场景 |
|---------|---------|---------|
| **高难度** | Claude Opus / GPT-4 | 复杂推理、代码重构 |
| **中等难度** | Claude Sonnet / Qwen3 | 常规对话、简单任务 |
| **低难度** | 本地模型 / MiniMax | 定时任务、批量处理 |

#### 3. 本地模型（终极零成本）

适合本地模型的场景：
- **定时任务**：晨报、新闻推送、定时提醒、社交媒体查看
- **每日复盘**：错误分析、对话质量、个人画像、新闻趋势
- **批量处理**：评论打标签、格式转换、摘要生成

**推荐硬件**：
- AMD 锐龙 AI MAX+ 395（128G 统一内存，96G 可拨给显存）
- Mac Studio 128G
- NVIDIA DGX Spark

**实测性能**：
- Qwen3-coder-next 80B：50 tokens/s
- Gemma 4 26B Q8：58页年报总结，80G 内存占用

---

## 养龙虾安全指南

### 风险分类

| 类型 | 比喻 | 说明 |
|-----|------|------|
| **外部风险** | 坏人骗助理 | 提示词注入、恶意 Skill、端口暴露 |
| **内部风险** | 助理好心办坏事 | 权限滥用、误操作、理解偏差 |

### 对外三件事

1. **不暴露端口**：默认端口 1xx9，问龙虾确认是否对外暴露
2. **不装来路不明 Skill**：只从 ClawHub 或火山引擎官方镜像站安装，安装前用 `skill-vetter` 扫描
3. **不开放外部输入**：群聊、社交平台回复、moltbook 都可能被提示词注入攻击

### 对内三件事

1. **安全检查**：
   ```bash
   openclaw security audit
   openclaw security audit --deep
   openclaw security audit --fix
   ```

2. **执行隔离**：Docker 中隔离执行，限制工具权限，提示词要求只在工作区操作

3. **账号隔离**：给龙虾单独申请专属账号（社交媒体、浏览器、Apple Store），不共享个人账号

### 长期建议

- 未来人人都要给自己的 Agent 准备工作站
- Agent 承载的需求越深，隐私要求越高
- 本地模型 + 专属设备是长期趋势