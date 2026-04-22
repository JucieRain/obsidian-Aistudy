---
title: "Hermes Agent 完整指南：从安装到进阶玩法，一篇搞定"
source: "https://zhuanlan.zhihu.com/p/2027128115831260939?utm_psn=2029550914726293928"
author:
  - "[[大模型爱好者社区大模型算法专家｜更多内容见公众号：机器学习社区]]"
published:
created: 2026-04-22
description: "这几天我们聊了很多 Hermes Agent 的设计哲学、部署和实战案例。有不少朋友在后台问： “装好之后还能干什么？”“怎么切换模型？”“我之前用龙虾的数据怎么迁过来？”“对话里那些斜杠命令都是干嘛的？”这篇就…"
tags:
  - "clippings"
---
[收录于 · 大模型技术](https://www.zhihu.com/column/c_1735673110735642626)

48 人赞同了该文章

目录

这几天我们聊了很多 Hermes Agent 的设计哲学、部署和实战案例。有不少朋友在后台问：

- “装好之后还能干什么？”
- “怎么切换模型？”
- “我之前用龙虾的数据怎么迁过来？”
- “对话里那些斜杠命令都是干嘛的？”

这篇就是你要的 **完整答案** ——不讲故事，纯干货。从环境检查到日常高频操作，一篇全覆盖。

顺便说一下数据：Hermes Agent 现在 [GitHub](https://zhida.zhihu.com/search?content_id=273031200&content_type=Article&match_order=1&q=GitHub&zhida_source=entity) 已经 **74K+ stars** ，最新版 **v0.8.0** ， [MIT 协议](https://zhida.zhihu.com/search?content_id=273031200&content_type=Article&match_order=1&q=MIT+%E5%8D%8F%E8%AE%AE&zhida_source=entity) 完全免费。增长速度是真的猛。

![](https://pic3.zhimg.com/v2-9ac34d34cf6966a9406b73749e515b72_1440w.jpg)

## 一、环境要求：先对照着查一遍

开始之前，花 30 秒确认一下你的系统能不能装：

![](https://pica.zhimg.com/v2-d28fef94f8fad0dacdce266b732cb212_1440w.jpg)

**Python 版本要求：3.11 或以上。**

如果你不确定自己的版本，终端输入 `python3 --version` 查一下。

没装或版本太低的，按下面装：

**macOS 用户** （推荐 Homebrew）：

```bash
brew install python@3.11
```

**Linux / WSL2 用户** ：

```bash
sudo apt update && sudo apt install python3.11 python3.11-venv
```

### 最新文章精选（关注、点赞、收藏，获取第一手信息）

[一路狂揽5.3万星的Hermes Agent 安装指南来了](https://zhuanlan.zhihu.com/p/2026310080262357049)

[装完Hermes Agent用了一下，OpenClaw真的可以退场了](https://zhuanlan.zhihu.com/p/2026051186134917689)

[（可能全网最全/长的）2万字Openclaw保姆教程](https://zhuanlan.zhihu.com/p/2012626589477781666)

[打工人必备 AI 新三件套：NotebookLM、Claude Code、Obsidian](https://zhuanlan.zhihu.com/p/2024133568557761035)

[我用两周时间踩完openclaw所有坑，总结出这份完整调教指南](https://zhuanlan.zhihu.com/p/2016823158380995920)

[OpenClaw 生产力翻倍：这20个技能太给力了](https://zhuanlan.zhihu.com/p/2017990909216714962)

[我用 OpenClaw 搞了家16人的公司：全员AI，24小时无休！](https://zhuanlan.zhihu.com/p/2018259939664109626)

[把 OpenClaw 装在本地电脑 24 小时工作，6000 字零基础上手教程](https://zhuanlan.zhihu.com/p/2019706301387666666)

[OpenClaw下载量 Top 20 的神仙级技能包分享](https://zhuanlan.zhihu.com/p/2019428885486388929)

[史上最全 OpenClaw 小龙虾常用操作命令指南](https://zhuanlan.zhihu.com/p/2021967648259408711)

[OpenClaw 十大痛点破解：10 个 Skills 直接对症下药](https://zhuanlan.zhihu.com/p/2022606975700145296)

[Claude Code 深度用法指南：那些让效率翻倍的隐藏技巧](https://zhuanlan.zhihu.com/p/2024783081865846798)

## 二、安装：一行命令，1-2 分钟

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

这个脚本会自动完成：

- 检测系统环境
- 安装必要依赖
- 下载 Hermes Agent 核心代码
- 把 `hermes` 命令注册到你的 PATH

装完之后 **当前终端还不认识 hermes 命令** ，需要重载一下：

```bash
# macOS（默认 zsh）
source ~/.zshrc

# Linux（默认 bash）
source ~/.bashrc
```

或者直接关掉终端重新打开，效果一样。

> ⚠️ **重要** ：不要用 `sudo` 跑安装脚本，用普通用户权限就行。加了 sudo 反而会出权限问题。

## 三、设置向导 + 模型配置

首次使用建议跑一遍完整的设置向导：

```bash
hermes setup
```

向导会引导你完成：

- 选择 LLM 提供商
- 填入 API Key
- 配置默认工具集
- 设置基础偏好
![](https://pic3.zhimg.com/v2-fe329e88f61d8fed9067000fda91284e_1440w.jpg)

### 模型切换：随时换，不改代码

Hermes 不绑定任何一家模型服务商。执行以下命令进入模型选择：

```bash
hermes model
```

会出现交互式菜单，选好服务商后填入 API Key。 **之后想切换模型随时可以再跑这条命令** 。

更灵活的是， **对话中也能临时切换模型** ：

```bash
/model openrouter:nous/hermes-3-405b
```

这意味着你可以在同一个对话里，先用便宜的模型跑初稿，再切到强模型做精修—— **精打细算的朋友狂喜** 。

### 国内模型也能用

选 Kimi / Moonshot / MiniMax，或者任何 **兼容 OpenAI API 格式** 的国内服务，走自定义端点就行。不用翻墙也能跑。

## 四、验证安装：hermes doctor

这个命令值得单独讲，因为它能省你 90% 的排错时间：

```bash
hermes doctor
```

它会逐项检查：

- Python 版本是否满足要求
- 依赖是否完整
- 模型配置是否有效
- 工具链是否正常

**全部绿色通过** = 装好了。有红色报错按提示修一下就行。

> 💡 **经验之谈** ：以后遇到任何问题，第一反应不要去搜论坛，先跑一遍 `hermes doctor` 。80% 的问题它能直接告诉你答案。

## 五、开始对话 + 对话中的进阶命令

一切就绪，启动：

```bash
hermes
```

进入交互式终端界面。支持多行编辑、斜杠命令自动补全、对话历史、流式输出。

试着让它干点活：

> “帮我写一个 Python 脚本，扫描当前目录下所有超过 100MB 的文件”

你会看到它调用内置工具，直接在终端里执行，结果实时输出。

### 日常必须知道的斜杠命令

这才是大多数教程不会告诉你的 **进阶玩法** ：

![](https://pic2.zhimg.com/v2-61bba20dcc09d9068160a95c2c29e365_1440w.jpg)

![](https://pic3.zhimg.com/v2-446b392e378113cd16659d626df0ad7e_1440w.jpg)

**重点说两个** ：

**`/skills`** —— 这是 Hermes “自进化”能力的可视化窗口。每当 agent 完成复杂任务后自动沉淀的技能，都能在这里看到。你用它一个月之后再敲这个命令，会被它积累的技能数量惊到。

**`/insights --days 7`** —— 相当于给你的 AI 助手出一份”周报”。它会总结这周它学到了什么、哪些技能被频繁调用、哪些任务模式在重复。 **这不是花哨功能，这是让你真正理解 agent 在如何进化的窗口** 。

## 六、多平台网关：一个进程管所有聊天工具

如果你想让 Hermes 同时在 Telegram、Discord、Slack 等平台上工作：

```bash
hermes gateway
```

一个 gateway 进程搞定所有平台。

**而且有个很狠的特性** ：它支持 **跨平台对话连续** ——在 Telegram 聊到一半，切到 Discord 继续， **上下文不丢** 。还支持语音消息转录。

这对什么人有用？做社群运营的朋友，你的客户可能分散在不同平台，但 Hermes 作为你的 AI 客服，在所有平台上记住的是同一份上下文。客户不管从哪个渠道找你，AI 都知道之前聊了什么。

## 七、从 OpenClaw 迁移：一行命令搞定

如果你之前用的是 OpenClaw（龙虾），Hermes 就是它的正式继任者。 **同一个团队，同一条产品线** ，但架构和能力做了大幅升级。

首次运行 `hermes setup` 时，如果检测到你本地有 `~/.openclaw` 目录，会自动提示迁移。

也可以手动操作：

```bash
# 交互式迁移（推荐）
hermes claw migrate

# 先预览不实际执行（胆小的用这个）
hermes claw migrate --dry-run

# 只迁移用户数据，不含密钥
hermes claw migrate --preset user-data
```
![](https://pic3.zhimg.com/v2-0ba051c8ebe63a82b55672fe1529fae2_1440w.jpg)

**迁移内容包括** ：

- 人格文件（SOUL.md）
- 记忆数据（MEMORY.md、USER.md）
- 自建技能（导入到 `~/.hermes/skills/openclaw-imports/` ）
- 命令审批白名单
- 各平台 API Key（Telegram、 [OpenRouter](https://zhida.zhihu.com/search?content_id=273031200&content_type=Article&match_order=1&q=OpenRouter&zhida_source=entity) 、OpenAI、 [ElevenLabs](https://zhida.zhihu.com/search?content_id=273031200&content_type=Article&match_order=1&q=ElevenLabs&zhida_source=entity) 等）
- TTS 语音资源
- 工作区指令（AGENTS.md）

> **迁移完成后 OpenClaw 的原始数据不会被删除** ，可以放心操作。万一不满意，原来的龙虾还在。

## 八、常见问题速查

![](https://pic2.zhimg.com/v2-d1162619d2dbb365e886645f9b2a7947_1440w.jpg)

## 九、给非技术读者的商业价值翻译

每次都要翻译一遍，因为这才是真正重要的部分。

**第一，”模型无关”是最大的保险。** Hermes 不绑定任何一家模型，意味着你今天用 [GPT-4](https://zhida.zhihu.com/search?content_id=273031200&content_type=Article&match_order=1&q=GPT-4&zhida_source=entity) ，明天 Claude 更强了切 Claude，后天国产模型够用了切国产省钱—— **你的 agent 积累的技能和记忆不受模型切换影响** 。这在 AI 变化这么快的今天，是最重要的一条护城河。

**第二，”跨平台上下文不丢”解决了客服最大的痛点。** 客户从微信问了一半，去 Telegram 又问一遍——传统客服要重新了解情况，Hermes 不用。 **一份记忆走天下** ，这才是 AI 客服该有的样子。

**第三，”龙虾一键迁移”说明生态在收敛。** 当一个新项目提供老项目的迁移工具，基本意味着它有信心成为最终胜出者。 **59K stars + MIT 协议 + 一键迁移** ，对个人和小公司来说，现在上车的风险已经很低了。

**第四， `/insights` 让 AI 第一次有了”周报”。** 你以前没法知道你的 AI 助手到底学了什么、成长了多少。现在可以了。 **这意味着 AI 员工的”绩效考核”第一次成为可能。** 管理 AI 不再是拍脑袋，而是有数据可看。

## 写在最后

这篇是 Hermes 系列的第四期，也是 **工具书性质** 的一期——收藏备查用的。

如果你按照前几期已经装好了 Hermes，这篇的价值在于让你知道 **装完之后还能干什么** 。如果你是第一次看到这个系列，这篇也足够你从零开始。

一句话总结 Hermes Agent 和其他 agent 框架最大的不同：

> **它不是一个工具，它是一个会成长的搭档。用得越多，它积累的技能和记忆越丰富，越来越像一个真正了解你工作方式的人。**

模型无关 + 多平台 + 持久记忆 + 自进化 —— 这四个词组合在一起，在开源 agent 框架里确实还没有第二个。

编辑于 2026-04-14 08:12・江苏