---
title: Hermes Agent
created: 2026-04-22
updated: 2026-05-01
sources:
  - "[[Clippings/articles/Hermes Agent 新手教程.md]]"
  - "[[Clippings/articles/Hermes + 飞书踩坑修复.md]]"
  - "[[Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md]]"
  - "[[Clippings/Hermes Agent 完整指南：从安装到进阶玩法，一篇搞定.md]]"
  - "[[Clippings/articles/给 10 万 Star 的 Hermes 装个记忆外挂，AI 终于能越用越聪明了]]"
  - "[[Clippings/articles/装完 Hermes 一定要配置这五套系统，秒变满配版，能力提升数倍不止]]"
  - "[[Clippings/papers/Hermes Agent 从入门到精通.pdf]]"
tags: [工具, Agent, NousResearch, 飞书, MemOS, 自改进, HarnessEngineering]
status: stable
---

# Hermes Agent

> 第一个出厂就带缰绳的 AI Agent——自己给自己造缰绳，缰绳会自己长大
> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §01

## 项目概览

| 项目信息 | |
|---------|---------|
| **开发者** | Nous Research |
| **GitHub Stars** | 10万+ |
> — Clippings/articles/给 10 万 Star 的 Hermes 装个记忆外挂，AI 终于能越用越聪明了。.md, L30
| **最新版本** | v0.8.0 |
| **协议** | MIT |
| **定位** | 模型无关 + 多平台 + 持久记忆 + 自进化 |

## 核心特性

- **自改进学习循环**：完成任务后自动复盘，策划记忆→创建Skill→Skill自改进→FTS5召回→用户建模
- **三层记忆架构**：会话记忆（发生了什么）→持久记忆（你是谁）→Skill记忆（怎么做事）
- **Skill 自进化**：从反馈中自动学习，不是等人维护；采用 agentskills.io 标准，与 Claude Code/Cursor 互通
- **模型无关**：随时切换模型（OpenRouter、OpenAI、Kimi、国产模型、本地Ollama）
- **多平台网关**：12+平台支持（飞书、Telegram、Discord、Slack、WhatsApp、Signal等）
- **跨平台上下文连续**：Telegram聊一半切Discord继续，上下文不丢
- **多Profile**：一个Agent多角色，专人专事
- **Honcho 用户建模**：可选外挂，辩证建模用户偏好（言行不一致也能捕捉）
- **MCP 集成**：6000+外部应用接入（GitHub、数据库、Slack、Jira等）

## 核心机制详解

### 学习循环：Agent 自己给自己造缰绳

Hermes 的核心创新是**自改进闭环**，五个环节串成飞轮：

```
策划记忆 → 创建 Skill → Skill 自改进 → FTS5 召回 → 用户建模
```

| 环节 | 职责 | 触发时机 |
|-----|------|---------|
| **策划记忆** | 主动决定哪些信息值得记住 | 每轮对话结束 |
| **创建 Skill** | 将解决方案提炼成可复用能力 | 完成复杂任务后 |
| **Skill 自改进** | 根据反馈自动优化 Skill 文件 | 使用 Skill 过程中 |
| **FTS5 召回** | 按需检索历史记忆，不全量加载 | 新对话开始时 |
| **用户建模** | 推导用户偏好、习惯、目标（Honcho） | 每次对话结束 |

关键区别：
- **传统 AI**：记忆是对话记录的堆积（录像带，越来越长最终溢出）
- **Hermes**：记忆是经验的蒸馏（笔记本，可以一直用下去）

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §03

### 三层记忆架构

| 层级 | 回答的问题 | 存储内容 | 技术实现 |
|-----|-----------|---------|---------|
| **会话记忆** | 发生了什么？ | 对话内容、工具调用、返回结果 | SQLite + FTS5 索引 |
| **持久记忆** | 你是谁？ | 编码偏好、项目结构习惯、常用工具链 | memory 工具管理 |
| **Skill 记忆** | 怎么做事？ | 方法论、操作规范 | ~/.hermes/skills/ markdown文件 |

三层对应认知科学的三种记忆类型：
- 情景记忆（Episodic）→ 会话记忆
- 语义记忆（Semantic）→ 持久记忆
- 程序性记忆（Procedural）→ Skill 记忆

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §04

### Skill 自改进机制

Skill 不是静态的，会在使用中自我进化：

1. **执行 Skill**：Agent 按 Skill 步骤完成任务
2. **收集反馈**：用户反应（满意/不满意/修正）被记录
3. **更新 Skill**：Agent 分析反馈，自动修改 Skill 文件
4. **下次生效**：改进后的 Skill 自动应用

与 Mitchell Hashimoto 的对比：
| 维度 | Mitchell 方式（手动） | Hermes 方式（自动） |
|-----|---------------------|-------------------|
| 规则来源 | 人观察到问题后手写 | Agent 自己从反馈中提炼 |
| 存储位置 | CLAUDE.md（单文件） | 多个 Skill 文件 + 记忆数据库 |
| 触发改进 | 人记得要加规则才会加 | 每次使用后自动评估 |
| 跨项目迁移 | 需要手动复制 | Skill 全局生效，所有项目共享 |

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §03, §05

### agentskills.io 互通标准

Hermes 采用 agentskills.io 标准，Skill 可跨工具迁移：

- **支持工具**：30+（Claude Code、Cursor、Copilot、Gemini CLI、Hermes 等）
- **意义**：你在 Claude Code 写的 Skill，Hermes 直接用；Hermes 自动创建的 Skill，也能拿到 Claude Code 用
- **Skill 不再绑定单一工具**：变成可移植的能力单元

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §05

### 与 Claude Code / OpenClaw 对比

三个工具不是三条路，是三匹马——各管一段：

| 维度 | Claude Code | OpenClaw | Hermes Agent |
|-----|-------------|----------|--------------|
| **核心理念** | 交互式编码 | 配置即行为（SOUL.md） | 自主后台 + 自改进 |
| **你的角色** | 坐在终端前指挥 | 写配置文件定义行为 | 部署后偶尔检查 |
| **记忆机制** | CLAUDE.md + auto-memory | 多层记忆（透明可控） | 三层自改进记忆 |
| **Skill 来源** | 手动安装 | ClawHub 44000+（人工维护） | Agent 自创 + 社区 Hub |
| **运行模式** | 按需启动 | 按需启动 | 24/7 后台运行 |
| **部署方式** | 本地 CLI（订阅制） | 本地 CLI（免费+API费） | $5 VPS / Docker / Serverless |
| **适合场景** | 写新功能、重构代码 | 团队标准化 Agent | 7x24代码审查、知识助手 |

一句话区分：
- **Claude Code 是工匠**（实时编码，你在场）
- **OpenClaw 是标准化框架**（配置透明，可审计）
- **Hermes 是管家**（后台自主，你不在它也在干活）

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §16

## 安装流程

### 三种部署方式

| 方式 | 适用场景 | 成本 | 启动时间 |
|-----|---------|------|---------|
| **本地安装** | 先体验再决定 | 仅 API 费 | 5分钟 |
| **Docker** | 隔离干净，状态持久 | 仅 API 贂 | 10分钟 |
| **$5 VPS** | 24/7在线，手机随时可达 | $5/月 + API费 | 15分钟 |

### $5 VPS 部署方案

推荐配置：

| VPS 提供商 | 月费 | 说明 |
|-----------|------|------|
| Hetzner CX22 | ~$4/月 | 性价比最高，欧洲节点 |
| DigitalOcean Droplet | $5/月 | 新加坡/美西节点 |
| Vultr | $5/月 | 东京节点延迟低 |

选 Ubuntu 22.04 LTS，不跑本地模型内存占用 <500MB，$5 机器绰绰有余。

配合 Telegram Gateway，手机上随时给 Hermes 发消息，它就在 VPS 上响应——一杯咖啡的钱，换一个24小时在线的 AI 助手。

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §02, §07

### Serverless 方案（进阶）

Hermes 支持 Daytona 和 Modal 两种 serverless 后端：
- 空闲时环境休眠，收到消息时自动唤醒
- 会话间成本趋近于零
- 在 config.yaml 设置 `terminal: daytona` 或 `terminal: modal`

> — Clippings/papers/Hermes Agent 从入门到精通.pdf, §07

### 官方安装脚本

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes version
hermes doctor
```

### 常见依赖问题

```bash
# 补基础依赖
cd ~/hermes-agent
./venv/bin/python -m pip install pyyaml python-dotenv

# 最小可用安装（文本链路）
./venv/bin/python -m pip install -e ".[feishu]"
```

## 飞书接入要点

### 配置步骤

1. 获取飞书应用 App ID 和 App Secret
2. 配置 `DASHSCOPE_API_KEY` 或其他模型密钥
3. 设置用户白名单或放开所有用户：
   ```bash
   hermes config set GATEWAY_ALLOW_ALL_USERS true
   ```

### 常见问题

| 问题 | 原因 | 解决方案 |
|-----|------|---------|
| 网关运行但不回复 | 用户白名单拦截 | 配置 FEISHU_ALLOWED_USERS |
| 401 错误 | 模型路由错误 | 检查 model.provider 配置 |
| av/cython 构建失败 | 多媒体依赖可选 | 使用最小安装，后续再补 |

## 模型配置

### DashScope（阿里云通义）

```bash
hermes config set model.provider alibaba
hermes config set model.default qwen3.5-plus
hermes config set DASHSCOPE_API_KEY "你的密钥"
```

### OpenRouter

```bash
hermes config set OPENROUTER_API_KEY "sk-or-v1-xxx"
```

## 文件结构

| 文件/目录 | 作用 |
|----------|------|
| **config.yaml** | Agent"人设"配置：模型、角色定位、工具、行为参数 |
| **.env** | 敏感信息：API Keys、网关令牌、数据库连接 |
| **profiles/** | 多个Agent独立配置 |
| **skills/** | Agent可调用的工具 |
| **memory/** | 记忆存储：每日记忆、长期记忆、Honcho外部记忆库 |
| **sessions/** | 会话历史，恢复对话状态 |
| **gateway/** | 消息平台连接配置 |

## 多Agent军团

### 核心原理

多Agent协同 = **角色隔离 + 共享上下文 + 任务委派**

| 组件 | 职责 | 类比 |
|-----|------|------|
| **Profiles** | 多Agent组织 | 公司部门 |
| **Gateway** | 消息收发通道 | 前台客服 |
| **Honcho** | 共享记忆 | 知识库 |
| **tmux** | 进程保活 | 灯一直开着 |

### 创建研发军团

```bash
hermes profile create commander        # 总管：调度、催办
hermes profile create market-director  # 市场总监：调研
hermes profile create product-director # 产品总监：PRD
hermes profile create architect-director # 架构总监：技术设计
hermes profile create dev-director     # 开发总监：代码实现
hermes profile create test-director    # 测试总监：验收
```

每个profile独立上下文，互不干扰。总管通过Honcho协调任务交接。

### 实战案例

苍何的Agent军团完成「电商竞品价格监控系统」：
- 市场调研 → PRD → 架构设计 → 开发实现 → 测试验收
- 开发总监自主调用Claude Code，7×24小时写代码
- Kimi K2.6在长任务场景表现稳定

详见 [[concepts/多Agent协同]]

## 斜杠命令

| 命令 | 作用 |
|-----|------|
| `/model xxx` | 对话中临时切换模型 |
| `/skills` | 查看积累的技能（自进化可视化） |
| `/insights --days 7` | Agent"周报"：学了什么、技能调用频率 |
| `/sethome` | 设置当前聊天为主频道 |

## 从OpenClaw迁移

```bash
# 交互式迁移
hermes claw migrate

# 预览不执行
hermes claw migrate --dry-run

# 只迁移用户数据
hermes claw migrate --preset user-data
```

迁移内容：人格、记忆、技能、命令审批白名单、API Keys、TTS资源。
迁移后OpenClaw原始数据不删除。

## 进阶配置：五大模块

裸装 Hermes 和满配 Hermes 完全是两种工具。五大配置模块：

| 模块 | 内容 | 效果 |
|-----|------|------|
| 身份与记忆 | SOUL.md、Hindsight | 让它知道你是谁 |
| 感知能力 | 内容抓取工具（Jina Reader、Crawl4 AI） | 让它读懂全网 |
| 表达能力 | 语音+图片生成（Whisper、Fal.ai） | 让它能说能画 |
| 效率与成本 | Tokscale、RTK | Token管控 |
| 生态导航 | awesome-hermes-agent | 一站式资源 |

### Hindsight 记忆系统

替换内置 MEMORY：
```bash
hermes memory setup
# 选择 hindsight
```

对比：内置 ≈2200字符硬上限 → Hindsight 无上限、知识图谱组织

### Token 管控工具

| 工具 | 功能 |
|-----|------|
| **Tokscale** | 实时 Token/成本监控 TUI |
| **RTK** | Rust Token Killer，减少60-90% Token |
| **hermes-hudui** | 按模型/组件/会话深度拆解成本 |

详见 [[practices/Hermes五大配置模块]]

## MemOS 记忆插件

记忆张量 MemTensor 团队推出的本地记忆插件：

### 核心能力

- **智能去重**：不是文本比对，是 LLM 判断重复/更新/全新
- **混合检索**：全文搜索 + 向量语义搜索
- **多Agent协同**：同一机器和跨机器两层协同

### 对比原生

| 维度 | Hermes 原生 | MemOS 插件 |
|-----|-------------|-----------|
| 写入 | Hermes认为重要才写 | 自动提取实体/事实/关系 |
| 检索 | SQLite文本匹配 | 混合检索引擎 |
| 协同 | 单Agent | 多Agent共享记忆 |

安装：
```bash
curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/openclaw-local-plugin-20260408/apps/memos-local-plugin/install.sh | bash
```

管理面板：http://127.0.0.1:18901

详见 [[tools/MemOS]]

## 常见问题速查

| 问题 | 解决 |
|-----|------|
| `hermes: command not found` | `source ~/.bashrc` |
| Python版本低 | 升级到3.11+ |
| API Key错误 | 检查.env配置 |
| 速率限制 | 降低请求频率或升级套餐 |
| OAuth过期 | 重新授权 |
| 上下文溢出 | 清理会话或换大模型 |
| Subagent超时 | 增加超时时间 |
| 记忆乱 | 安装 MemOS 插件做智能去重 |

诊断命令：`hermes doctor`（解决80%问题）

## 商业价值

- **模型无关**：今天GPT-4，明天Claude，后天国产省钱——积累的技能和记忆不受影响
- **跨平台上下文不丢**：客服场景，客户从微信切Telegram继续
- **`/insights`周报**：AI员工"绩效考核"首次成为可能
- **一键迁移**：OpenClaw用户无门槛升级

## 在知识库中的应用

- **素材收集**：爬取视频字幕、网页内容
- **跨设备同步**：通过GitHub同步到Obsidian Vault
- **多Agent军团**：研发流程自动化
- **飞书集成**：远程素材输入

## 参见

- [[tools/Claude Code]] - 开发Agent可调用，交互式编码
- [[tools/飞书]] - 消息渠道
- [[tools/OpenClaw]] - 前代产品（可迁移），配置即行为
- [[tools/MemOS]] - 记忆插件，智能去重+混合检索
- [[concepts/Agent]] - Agent基础概念
- [[concepts/多Agent协同]] - 军团架构详解
- [[concepts/长期记忆]] - Honcho记忆系统
- [[concepts/学习循环]] - 自改进Agent核心机制
- [[concepts/Harness Engineering]] - 缰绳工程方法论
- [[concepts/agentskills.io]] - Skill互通标准
- [[people/花叔]] - 橙皮书作者
- [[people/Mitchell Hashimoto]] - Harness Engineering理念创始人
- [[people/逛逛]] - MemOS插件推荐者
- [[people/科技君]] - 五大配置模块教程作者
- [[practices/Hermes五大配置模块]] - 进阶配置指南

## 来源

- [[Clippings/articles/Hermes Agent 新手教程.md]]
- [[Clippings/articles/Hermes + 飞书踩坑修复.md]]
- [[Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md]]
- [[Clippings/Hermes Agent 完整指南：从安装到进阶玩法，一篇搞定.md]]
- [[Clippings/articles/给 10 万 Star 的 Hermes 装个记忆外挂，AI 终于能越用越聪明了]]
- [[Clippings/articles/装完 Hermes 一定要配置这五套系统，秒变满配版，能力提升数倍不止]]
- [[Clippings/papers/Hermes Agent 从入门到精通.pdf]] — 橙皮书 v260407，花叔著