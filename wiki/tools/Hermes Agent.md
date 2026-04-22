---
title: Hermes Agent
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Hermes Agent 新手教程.md]]"
  - "[[Clippings/articles/Hermes + 飞书踩坑修复.md]]"
  - "[[Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md]]"
  - "[[Clippings/Hermes Agent 完整指南：从安装到进阶玩法，一篇搞定.md]]"
tags: [工具, Agent, NousResearch, 飞书]
status: stable
---

# Hermes Agent

> Nous Research 推出的开源 AI Agent，74K+ Stars，支持多平台消息网关、多Profile、长期记忆

## 项目概览

| 项目信息 | |
|---------|---------|
| **开发者** | Nous Research |
| **GitHub Stars** | 74K+ |
| **最新版本** | v0.8.0 |
| **协议** | MIT |
| **定位** | 模型无关 + 多平台 + 持久记忆 + 自进化 |

## 核心特性

- **模型无关**：随时切换模型（OpenRouter、OpenAI、Kimi、国产模型）
- **多平台网关**：飞书、Telegram、Discord、Slack
- **跨平台上下文连续**：Telegram聊一半切Discord继续，上下文不丢
- **多Profile**：一个Agent多角色，专人专事
- **持久记忆**：Honcho共享记忆 + Skills沉淀
- **自进化**：复杂任务自动沉淀技能

## 安装流程

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

- [[tools/Claude Code]] - 开发Agent可调用
- [[tools/飞书]] - 消息渠道
- [[tools/OpenClaw]] - 前代产品（可迁移）
- [[concepts/Agent]] - Agent基础概念
- [[concepts/多Agent协同]] - 军团架构详解
- [[concepts/长期记忆]] - Honcho记忆系统

## 来源

- [[Clippings/articles/Hermes Agent 新手教程.md]]
- [[Clippings/articles/Hermes + 飞书踩坑修复.md]]
- [[Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md]]
- [[Clippings/Hermes Agent 完整指南：从安装到进阶玩法，一篇搞定.md]]