---
title: OpenClaw 养成路线图
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/OpenClaw 养成路线图：从装完到用好的 8 个阶段.md]]"
tags:
  - practice
  - openclaw
  - agent
  - tutorial
status: stable
---

# OpenClaw 养成路线图

> 从安装到熟练使用的8个阶段，每个阶段有明确"毕业标准"

## 认知前提

OpenClaw不是"开箱即用"的工具，更像一个"毛坯房"。需要用户逐步配置和"养成"。

核心文件：
- **CLAUDE.md** - Agent"行为宪法"
- **Memory** - 记忆存储
- **Skills** - 能力扩展

路径是确定的：按顺序走，每个人都能养出一只好用的龙虾。

## 8个阶段概览

| 阶段 | 核心任务 | 预计耗时 |
|-----|---------|---------|
| **1.落地安装** | 跑起来，能对话 | 1-2小时 |
| **2.安全防护** | 红线规则 + 每晚巡检 | 1-2小时 |
| **3.身份设定** | 写CLAUDE.md | 30分钟 |
| **4.技能装备** | 装5核心Skill + 安全审计 | 1-2小时 |
| **5.记忆塑造** | 搭建三层记忆 | 1-3小时 |
| **6.自动化接管** | Hooks + Cron | 2-4小时 |
| **7.多Agent协作** | Workspace隔离 | 3-5小时 |
| **8.持续进化** | 反思 + 迭代 | 长期 |

总投入：**11-19小时**

## 阶段1：落地安装

### 三种安装方案

| 方案 | 适合用户 | 方式 |
|-----|---------|------|
| **命令行** | 有终端经验 | `npm install -g openclaw` |
| **ClawPanel** | 恐惧命令行 | Tauri桌面应用，一键安装配置诊断 |
| **Mac mini** | 24小时运行 | 低功耗、M芯片够用、SSH远程访问 |

### 环境要求

- Node.js ≥ 22.0.0
- Python 3.9 - 3.11（3.12部分插件不兼容）
- Docker ≥ 20.10.0（可选）

### 避坑提醒

1. **版本兼容性是第一杀手**：部署前先跑 `node -v` 和 `python3 --version`
2. **网络环境**：国内用户注意配置代理
3. **不要在主力机裸跑**：建议虚拟机或独立设备
4. **报错先跑 `openclaw doctor`**：自动诊断大部分问题

### 毕业标准

- [ ] 成功启动，能正常对话
- [ ] 配置了一个模型
- [ ] 能通过至少一个渠道交互

## 阶段2：安全防护

### 红线命令（遇到必须暂停）

```
## 安全红线（遇到必须向我确认）
### 破坏性操作
- `rm -rf /` 或 `rm -rf ~`
- `mkfs`、`dd if=`、`wipefs`
- 直接写块设备

### 认证篡改
- 修改 `openclaw.json` 认证字段
- 修改 `sshd_config` 或 `authorized_keys`

### 外发敏感数据
- `curl/wget` 携带 token/key/password 发往外部
- 反弹 shell (`bash -i >& /dev/tcp/`)
- `scp/rsync` 往未知主机传文件

### 代码注入
- `curl | sh` 或 `wget | bash`
- `eval "$(curl ...)"`
- 可疑的 `base64 -d | bash`

### 权限持久化
- `crontab -e`（系统级）
- `useradd/usermod/passwd`
- `systemctl enable` 新增未知服务
```

### 黄线命令（可执行但必须记录）

- 任何 `sudo` 操作
- `pip install` / `npm install -g`
- `docker run`
- `systemctl restart/start/stop`
- `chattr -i` / `chattr +i`

### 每晚自动巡检

设置凌晨3点自动检查13项核心指标：
1. OpenClaw配置文件完整性
2. 进程与网络监听端口
3. 敏感目录文件变更
4. 系统定时任务
5. 登录记录与SSH失败尝试
6. 关键文件哈希基线对比
7. 黄线操作交叉验证
8. 磁盘使用率
9. Gateway环境变量检查
10. 明文私钥泄露扫描
11. Skill/MCP完整性
12. 大脑灾备自动同步

**重要**：即使所有指标正常，巡检也会推送完整报告。避免"无异常则不汇报"产生猜疑。

### 毕业标准

- [ ] CLAUDE.md写入红线黄线规则
- [ ] 配置每晚自动巡检
- [ ] 设置核心文件权限保护
- [ ] 实测龙虾执行危险操作会先问

## 阶段3：身份设定

### 写第一份CLAUDE.md

```markdown
# 我的AI助手
## 角色
你是我的个人工作助手，帮我处理日常任务。

## 行为准则
- 回复简洁，不说废话
- 不确定的信息标注[待核实]
- 重要操作前先确认
- 不要编造数据和链接

## 我的信息
- 职业：[你的职业]
- 常用工具：[你的工具]
- 工作习惯：[你的偏好]
- 沟通风格：[直接/详细/轻松]
```

**为什么重要？**

没有CLAUDE.md的龙虾每次从零开始。有了它，龙虾每次启动都带着"对你的理解"。

### 分层设计

```
~/.claude/CLAUDE.md          ← 全局设定
项目A/.claude/CLAUDE.md      ← 项目级设定
项目B/.claude/CLAUDE.md      ← 覆盖规则
```

### 毕业标准

- [ ] 创建了全局CLAUDE.md
- [ ] 写了至少3条行为准则
- [ ] 填写了基本信息
- [ ] 实测回复风格发生变化

## 阶段4：技能装备

### 技能生态（截至2026年3月）

- ClawHub官方商店：5,700+技能，日安装15,000+
- Awesome OpenClaw Skills：5,490+技能，31类别

### 新手必装5个Skill

| Skill | 作用 | 安装命令 |
|-------|------|---------|
| **tavily-search** | 联网搜索 | `npx clawhub@latest install tavily-search` |
| **browser-use** | 浏览器控制 | `npx clawhub@latest install browser-use` |
| **find-skills** | 自动发现技能 | `npx clawhub@latest install find-skills` |
| **memory-manager** | 记忆增强 | ClawHub搜索安装 |
| **agent-reach** | 全平台连接器 | ClawHub搜索安装 |

### 安装前安全审计（5步）

1. `clawhub inspect <skill> --files` 列出所有文件
2. `clawhub install <skill> --dry-run` 预览下载位置
3. **全文本排查**：Markdown和JSON也要检查
4. 检查红线行为：curl|sh、读取环境变量、外发数据
5. 向自己汇报审计结果

**3个危险信号**：
- 安装量低(<100)但功能强大
- 作者账号新注册
- 大段base64编码内容

### 毕业标准

- [ ] 安装了至少3个Skill
- [ ] 包含搜索类Skill
- [ ] 实测用Skill完成过真实任务

## 阶段5：记忆塑造

### 三层记忆架构

| 层级 | 内容 | 生命周期 | 存储 |
|-----|------|---------|------|
| **L0短期** | 当前对话 | 单次会话 | 自动管理 |
| **L1中期** | 会话摘要 | 跨会话 | memory/目录 |
| **L2长期** | 用户偏好 | 永久 | CLAUDE.md + 知识库 |

大部分用户只用L0。对话结束就什么都不记得。

### 搭建目录

```
~/.claude/memory/
├── MEMORY.md          ← 核心记忆（自动加载）
├── patterns.md        ← 工作模式习惯
├── projects.md        ← 项目知识
└── preferences.md     ← 偏好设置
```

### MEMORY.md模板

```markdown
# 记忆
## 工作习惯
- 早上9点开始，下午6点结束
- 喜欢Markdown格式，代码块三反引号
- 代码风格：简洁优先，不写多余注释
- 讨厌被问"需要我解释吗"

## 项目上下文
- 当前项目：AI内容工厂
- 技术栈：Python 3.11 + Node.js 22
- 截止日期：2026-03-15

## 常用命令
- 启动：`npm run dev`
- 测试：`npm test -- --watch=false`
- 部署：`./deploy.sh production`
```

### 毕业标准

- [ ] 创建memory/目录结构
- [ ] MEMORY.md至少10条有效记忆
- [ ] 龙虾能在新会话引用记忆
- [ ] 配置"主动记忆"规则

## 阶段6：自动化接管

### Hooks：事件触发

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit",
      "command": "npx prettier --write $FILE_PATH"
    }]
  }
}
```

实际场景：
- 代码保存后自动格式化
- Git提交前检查敏感信息
- 每次对话开始显示时间和项目状态

### Cron：定时执行

**每天早上8点汇总新闻**：
```bash
openclaw chat "帮我汇总今天的科技新闻，保存到 daily-brief/$(date +%Y%m%d).md"
```

**每周一生成工作报告**：
```bash
openclaw chat "读取git log --since='1 week ago'，生成上周工作总结"
```

### 毕业标准

- [ ] 配置至少2个Hooks
- [ ] 设置至少1个定时任务
- [ ] 自动化任务稳定运行3天+
- [ ] 花钱和对外操作配置人工确认

## 阶段7：多Agent协作

### 四种分身模式

| 模式 | 场景 | 实现 |
|-----|------|------|
| **多Workspace** | 项目隔离 | 不同目录各有CLAUDE.md |
| **Sub-agents** | 临时子任务 | 主Agent调度子Agent |
| **多Gateway** | 独立运行 | 不同端口各有人格 |
| **定时Agent** | 后台自动 | Cron + 独立配置 |

### Workspace隔离示例

```
~/work/
├── project-a/.claude/CLAUDE.md   ← 项目A Agent
├── project-b/.claude/CLAUDE.md   ← 项目B Agent
└── personal/.claude/CLAUDE.md    ← 个人助手
```

每个目录进去就是"不同的龙虾"，记忆互不干扰。

### 毕业标准

- [ ] 至少2个独立Workspace
- [ ] 每个有独立CLAUDE.md和Memory
- [ ] 不同Agent不"串记忆"

## 阶段8：持续进化

### 反思日志

每次完成重要任务，让龙虾自我复盘：
- 哪些做得好
- 哪些可改进
- 结论写入Memory

### 模式识别

发现重复模式固化为规则：
- 每次写文章都先列大纲 → 写入CLAUDE.md默认流程
- 每次审校都检查错别字 → 写成Hook自动执行
- 某Prompt效果好 → 保存为Skill

### 定期迭代

每月花30分钟审查CLAUDE.md：
- 删除过时规则
- 补充新规则
- 清理过期Memory

### 终极毕业标准

- [ ] CLAUDE.md超过50行有效规则
- [ ] Memory目录5+分类文件
- [ ] 3个稳定运行的自动化任务
- [ ] 定期迭代优化配置
- [ ] 能根据新需求扩展能力

## 社区资源

- **ClawHub**（clawhub.ai）：日安装15,000+
- **Awesome OpenClaw Skills**：GitHub 29K Stars
- **OpenClaw Showcase**：看别人怎么用

## 参见

- [[tools/OpenClaw]] - 工具详情页
- [[concepts/长期记忆]] - 记忆系统设计
- [[concepts/多Agent协同]] - Hermes版本对比
- [[practices/工具模型配置汇总]] - 模型配置方法

## 来源

- [[Clippings/OpenClaw 养成路线图：从装完到用好的 8 个阶段.md]]