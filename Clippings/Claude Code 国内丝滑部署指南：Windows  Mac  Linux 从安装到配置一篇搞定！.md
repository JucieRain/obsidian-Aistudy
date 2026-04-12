---
title: "Claude Code 国内丝滑部署指南：Windows / Mac / Linux 从安装到配置一篇搞定！"
source: "https://zhuanlan.zhihu.com/p/2026324346390557144"
author:
  - "[[AI折腾指南持续记录 AI 工具、部署配置、实战体验和踩坑过程]]"
published:
created: 2026-04-11
description: "最近在折腾终端里的 AI 编程工具时，发现不少人不是不会用 Claude Code，而是第一步就卡在了 安装、配置、环境变量 这些细节上。尤其是 Windows 用户，最容易遇到的就是： 装完了却识别不到 claude配好了 Key 还是…"
tags:
  - "clippings"
---
最近在折腾终端里的 AI 编程工具时，发现不少人不是不会用 **Claude Code** ，而是第一步就卡在了 **安装、配置、环境变量** 这些细节上。

尤其是 Windows 用户，最容易遇到的就是：

- 装完了却识别不到 `claude`
- 配好了 Key 还是提示 `Invalid API Key`
- 明明能启动，但状态显示 `offline`
- 想让它稳定跑起来，结果卡在网络或配置文件路径上

所以这篇就把 **Claude Code 的安装、配置、启动和常见报错** 按顺序整理一遍。 尽量保留最原始的操作逻辑，方便你直接照着走。

## Claude Code 安装使用教程

Claude Code 是一个很强的 AI 编程助手，可以直接在终端里和 AI 协作写代码。 如果你平时本来就习惯用命令行、Git、编辑器和项目目录，那它的体验会很顺手。

这篇教程主要带你完成两件事：

- **先装好 Claude Code**
- **再把配置补齐，确保能真正跑起来**

## 📋 系统要求

在开始之前，先确认一下你的环境是否满足要求。

- **支持的操作系统：** macOS 10.15+、Ubuntu 20.04+ / Debian 10+、Windows 10+（带 WSL 或 [Git for Windows](https://zhida.zhihu.com/search?content_id=272915167&content_type=Article&match_order=1&q=Git+for+Windows&zhida_source=entity) ）
- **硬件要求：** 4GB+ RAM
- **软件要求：** Git（Windows 安装需要）、Node.js 18+（仅 NPM 安装需要）
- **网络要求：** 需要具备 Anthropic 支持国家 / 地区的网络连接

## 🚀 安装 Claude Code

目前更推荐使用 **原生安装** 的方式，原因比较直接：

- ✅ 一个自包含的可执行文件
- ✅ 不依赖 Node.js
- ✅ 自动更新更稳定

如果你之前已经装过旧版本 Claude Code，可以运行下面这条命令迁移到原生二进制安装：

```bash
claude install
```

## Windows 系统安装步骤

### 步骤 1：安装 Git for Windows

在 Windows 上原生安装 Claude Code，通常需要通过 **Git Bash** 来配合完成。

Git for Windows 下载地址： `https://git-scm.com/install/windows`

下载对应系统版本后，按默认选项一路安装即可。 安装完成后，可以先验证一下：

```
git --version
```

### 步骤 2：安装 Claude Code

安装好 Git 之后，打开 **PowerShell** 或 **CMD** ，运行下面的安装命令。

### Windows PowerShell 安装命令

```
irm https://claude.ai/install.ps1 | iex
```

### Windows CMD 安装命令

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

如果上面两种方式都不行，还可以直接试这个：

```
winget install Anthropic.ClaudeCode
```

### 步骤 3：添加 PATH 环境变量

这一步是 Windows 用户最容易漏掉的地方。

Claude 可执行文件所在目录需要加入系统 `PATH` ，否则 PowerShell 可能识别不到 `claude` 命令。

参考路径：

```
C:\Users\你的用户名\.local\bin
```

添加方式如下：

**打开系统属性 → 环境变量 → 编辑用户 PATH → 新建 → 添加上面的 Claude 安装路径**

这里建议把这一步配好之后， **重启 PowerShell 终端** 。 如果还是不生效，直接重启电脑，通常就正常了。

![](https://pic4.zhimg.com/v2-35b0f17adc5c8a28bd8484904f91d607_1440w.jpg)

## macOS / Linux 系统安装步骤

如果你是 macOS、Linux 或 WSL 环境，安装会简单很多。

### macOS / Linux / WSL 安装命令

```
curl -fsSL https://claude.ai/install.sh | bash
```

### Homebrew（macOS / Linux）安装命令

```
brew install --cask claude-code
```

## 💡 补充：也可以用 NPM 安装

如果你本机已经安装了 **Node.js 18.0 或更高版本** ，也可以直接使用 NPM 安装：

```
npm install -g @anthropic-ai/claude-code
```

安装完成后，打开一个新的终端，输入下面这条命令验证是否安装成功：

```
claude --version
```

## ⚙️ 配置并开始使用

装好只是第一步。 想让 Claude Code 真正跑起来，还需要把配置项补完整。

你需要准备下面两个核心配置项：

📌 **注册入口： [LetAiCode中转站](https://link.zhihu.com/?target=https%3A//letaicode.cn/%3Faff%3DKbmuqF) （重要！！！）**

| 配置项 | 说明 | 获取方式 |
| --- | --- | --- |
| [ANTHROPIC\_AUTH\_TOKEN](https://zhida.zhihu.com/search?content_id=272915167&content_type=Article&match_order=1&q=ANTHROPIC_AUTH_TOKEN&zhida_source=entity) | API 认证令牌 | 注册后在接口密钥页面点击“创建新密钥”获得，选择 Claude Code 类型，令牌通常以 sk- 开头 |
| [ANTHROPIC\_BASE\_URL](https://zhida.zhihu.com/search?content_id=272915167&content_type=Article&match_order=1&q=ANTHROPIC_BASE_URL&zhida_source=entity) | API 服务地址 | 使用 [letaicode.cn/claude](https://link.zhihu.com/?target=https%3A//letaicode.cn/claude) |

## 🗂 配置文件位置

然后新建或修改 `settings.json` 配置文件。

配置文件路径如下：

- **Windows：** `C:\Users\用户名\.claude\settings.json`
- **Mac：** `~/.claude/settings.json`
- **Linux：** `~/.claude/settings.json`

把下面这段内容写进去即可。 其中：

- `ANTHROPIC_AUTH_TOKEN` 替换成你的实际 API 令牌
- `ANTHROPIC_MODEL` 可以按需替换为你想用的模型 ID
```
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-你的API令牌",
    "ANTHROPIC_BASE_URL": "https://letaicode.cn/claude",
    "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929",
    "ANTHROPIC_SMALL_FAST_MODEL": "claude-haiku-4-5-20251001"
  }
}
```

如果你用的是 Ubuntu 或 macOS，也可以直接通过 `vi` 或 `vim` 创建 / 修改这个文件：

```
vim ~/.claude/settings.json
```

## ▶️ 启动 Claude Code

配置完成后，进入你的项目目录，直接运行：

```
cd /path/to/your/project
claude
```

这样就可以启动 Claude Code 了。

## 🧩 初次运行配置

第一次启动时，通常会看到一组初始化配置流程，按提示走就行：

- **选择主题** → 选择你喜欢的主题，然后按 Enter
- **安全须知** → 确认安全须知，然后按 Enter
- **Terminal 配置** → 默认即可，按 Enter
- **工作目录信任** → 信任当前目录，按 Enter

到这里，Claude Code 就已经可以正常开始用了。

✨ **恭喜，接下来你就可以直接在终端里和 AI 一起写代码了。**

## ❓ 常见问题解答

### Q1：遇到 Invalid API Key · Please run /login 错误怎么办？

这通常说明 Claude Code 没有正确读取到环境变量。

优先检查这几项：

- 是否正确设置了 `ANTHROPIC_AUTH_TOKEN` 和 `ANTHROPIC_BASE_URL`
- 令牌内容是否正确，且确实是以 `sk-` 开头
- 如果你改的是永久配置文件，改完后有没有 **重启终端**

很多时候不是 Key 本身有问题，而是配置改了之后终端还在读旧环境。

### Q2：PowerShell 无法安装脚本，提示执行策略错误怎么办？

可以用 **管理员身份** 启动 PowerShell，然后执行：

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

执行完之后，再重新运行安装命令即可。

### Q3：为什么会显示 offline 状态？

这是很多人第一次看到都会误会的一个点。

Claude Code 会通过连接 Google 来判断网络状态， 所以显示 `offline` **不一定代表不能用** ，更多只是说明当前环境无法连接到 Google。

也就是说：

- **显示 offline ≠ Claude Code 一定不可用**
- 只要 API 调用正常，很多情况下照样能跑

### Q4：为什么浏览网页时 Fetch 会失败？

Claude Code 在访问网页之前，会先调用 Claude 服务做一次安全检查。 所以这类功能对网络环境要求会更高一些。

一般需要注意两点：

- 保持相对稳定的国际网络连接
- 必要时使用全局代理

### Q5：请求总是报 fetch failed 怎么办？

这类问题多数还是网络环境导致的。

可以先这样排查：

- 尝试开启代理工具
- 换一个更稳定的网络环境
- 重新启动 Claude Code 再试一次

### Q6：API 报错怎么处理？

如果你使用的是代理转发服务，偶尔也可能出现链路不稳定的情况。

常见处理方式：

1. 先退出 Claude Code
```
Ctrl + C
```
1. 再重新执行：
```
claude
```

如果重试之后还是不行，通常建议稍后再试。

### Q7：网页登录报错怎么办？

这个问题一般比较直接，优先尝试下面这个办法：

很多网页端登录问题，清 Cookie 之后就恢复正常了。

## 🔗 相关链接

- [Claude Code 官方文档](https://link.zhihu.com/?target=https%3A//platform.claude.com/docs/en/home)
- [Node.js 官方网站](https://link.zhihu.com/?target=https%3A//nodejs.org/)

## 💡 最后补一句

Claude Code 本身不算难装，真正容易出问题的，其实是这几个地方：

- Windows 下的 PATH 没加
- `settings.json` 路径写错
- API Key 填错或没重启终端
- 网络状态不稳定，导致 fetch 或登录异常

把这几个点理顺之后，后面基本就顺了。

发布于 2026-04-11 20:26・广东