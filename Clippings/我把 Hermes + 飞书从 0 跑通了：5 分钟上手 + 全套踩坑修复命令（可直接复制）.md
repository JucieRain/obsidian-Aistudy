---
title: "我把 Hermes + 飞书从 0 跑通了：5 分钟上手 + 全套踩坑修复命令（可直接复制）"
source: "https://juejin.cn/post/7626213394731827219"
author:
  - "[[测试员周周]]"
published: 2026-04-09
created: 2026-04-11
description: "我把 Hermes + 飞书从 0 跑通了：5 分钟上手 + 全套踩坑修复命令（可直接复制） 大家好，我是测试员周周，全网同名。 这是 Hermes 系列第 2 篇，也是实操篇。 如果你也遇到过这些场"
tags:
  - "clippings"
---
大家好，我是测试员周周，全网同名。

---

这是 Hermes 系列第 2 篇，也是实操篇。

如果你也遇到过这些场景，这篇就是给你写的：

- Hermes 装好了，但飞书机器人不回
- `gateway` 明明是 running，发消息还是没反应
- 一开口就是 401，看不懂到底是飞书错还是模型错

上一篇我们讲“为什么 Hermes 火”，这一篇只做一件事： **让你真的跑起来** 。

我会把这次真实实操里踩过的坑全部摊开，包括：

- 安装后 `No module named yaml/dotenv` 怎么修
- `av/cython` 报错时怎么先绕过，优先跑通文本链路
- 飞书网关明明 running，为什么还是不回消息
- 最容易误判的 401：为什么会跑到 OpenRouter 而不是 DashScope

你照着本文走，最终会拿到：

- 一个可用的 Hermes 环境（ `hermes doctor` 可验证）
- 一个可在飞书里回复消息的机器人（有日志可追踪）
- 一份可复用的“问题 -> 命令 -> 验证”排障模板

我承诺一个结果：你不需要靠猜，只要按命令做，就能定位到问题在哪一层（安装层、网关层、模型层）。

开始之前，确认你的环境：

- Linux / macOS / WSL2（官方推荐路径；原生 Windows 不支持，请用 WSL2）
- 已安装 Git（ `git --version` 可用）
- 至少 1 个可用 LLM Provider API Key（如 OpenRouter / OpenAI / 阿里云 DashScope 等）
- 如果要接飞书，请提前准备好飞书应用的 `App ID` 和 `App Secret`
- 基础命令行能力

文中凡是出现 `~/hermes-agent` 的地方，均指你克隆或解压 Hermes 仓库后的 **项目根目录** ；若路径不同，请自行替换（官方手动安装示例： `git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git` 后进入 `hermes-agent` ）。

**命令校对说明（请务必看一眼）** ：下文与 **两套公开文档** 对齐校验过——

- Nous Research **官方英文文档** （入口）： [hermes-agent.nousresearch.com/docs/](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2F "https://hermes-agent.nousresearch.com/docs/")
- 安装与验证： [Installation](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2Fgetting-started%2Finstallation "https://hermes-agent.nousresearch.com/docs/getting-started/installation") （Step 10 示例含 `hermes chat -q "Hello! ..."` ）

\- **配置目录、 `hermes config` 、优先级（config.yaml /.env）** ： [Configuration](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2Fuser-guide%2Fconfiguration "https://hermes-agent.nousresearch.com/docs/user-guide/configuration")

\- **推理提供商与密钥命名（含阿里云 Alibaba / DashScope）** ： [AI Providers](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2Fintegrations%2Fproviders "https://hermes-agent.nousresearch.com/docs/integrations/providers")

- 消息网关、systemd、 `journalctl` 、 `GATEWAY_ALLOW_ALL_USERS` 、 **`hermes-feishu`** ： [Messaging Gateway](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2Fuser-guide%2Fmessaging "https://hermes-agent.nousresearch.com/docs/user-guide/messaging")
- **中文文档镜像** ： [hermes-doc.aigc.green/](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2F "https://hermes-doc.aigc.green/")

\- [安装](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2Fgetting-started%2Finstallation "https://hermes-doc.aigc.green/getting-started/installation") · [配置说明](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2Fuser-guide%2Fconfiguration "https://hermes-doc.aigc.green/user-guide/configuration") · [AI 模型提供商](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2Fintegrations%2Fproviders "https://hermes-doc.aigc.green/integrations/providers") · [消息网关](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2Fuser-guide%2Fmessaging "https://hermes-doc.aigc.green/user-guide/messaging")

在此基础上，文中与 **Hermes 0.7.x 仓库 `pyproject.toml`** 做了交叉核对（例如可选依赖 **`[feishu]`** ：安装页「extras 表格」可能未逐条列出飞书；以仓库为准， **`uv pip install -e ".[all]"` 已包含 `feishu`** ）。

你本地仍请以 `hermes --help` 、 `hermes chat --help` 、 `hermes gateway --help` 为准。 `sed -i` 在 **macOS** 上需写成 `sed -i '' '...'` 。从网页或 PDF 复制命令时，请确认 **引号成对、整行完整** 。

如果你也想少走弯路，直接开始。

---

环境配置（Ubuntu 实操版，5-15 分钟）

第一步：先走官方安装（推荐）

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# 重新加载 shell（bash / zsh 二选一）
source ~/.bashrc
# source ~/.zshrc

# 验证命令是否可用
hermes version
hermes doctor
```

预期结果：

- `hermes version` 返回版本号
- `hermes doctor` 诊断通过或仅提示非阻塞项

失败分支：

- 如果提示 `command not found` ，先执行 `source ~/.bashrc` （或对应 shell 配置）后重试
- 如果 doctor 报依赖缺失，进入第二步兜底修复

第二步：如果官方安装后命令异常，按下面兜底修复（可直接复制）

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码cd ~/hermes-agent

# 1) 给当前 venv 补 pip
./venv/bin/python -m ensurepip --upgrade

# 2) 升级 pip 基础工具
./venv/bin/python -m pip install -U pip setuptools wheel

# 3) 先装关键缺失依赖（常见缺 yaml / env；核心已在项目依赖里，此行属兜底）
./venv/bin/python -m pip install pyyaml python-dotenv

# 4) 安装项目完整依赖（推荐；官方文档等价命令为 uv pip install -e ".[all]"）
./venv/bin/python -m pip install -e ".[all]"

# 5) 如仍缺基础包，可显式补齐
./venv/bin/python -m pip install python-dotenv pyyaml click rich pydantic

# 6) 验证 CLI 可用（若已将 venv/bin/hermes 链到 ~/.local/bin，可直接用 hermes …）
./venv/bin/python -m hermes_cli.main --version
./venv/bin/python -m hermes_cli.main gateway setup
# 无前缀子命令时等价于 gateway run：前台跑网关；若使用 systemd 用户服务见后文 start/stop
./venv/bin/python -m hermes_cli.main gateway
```

预期结果：

- `--version` 正常返回版本
- `gateway setup` 可进入配置流程
- `gateway` 可正常启动或给出可理解提示

失败分支：

- 如果仍报 `No module named ...`，重新执行第 4 步 `pip install -e ".[all]"`
- 如果仍报 `yaml/dotenv` 缺失，重复第 3 步补包并重试
- 如果网络相关依赖下载失败，切换网络后重跑第 4 步

补充说明（很多人会卡在这里）：

- 如果 `pip install -e ".[all]"` 报 `av/cython` 构建失败，通常不是 Hermes 主体损坏，而是可选的多媒体依赖安装失败。
- `cython` 是构建部分 C 扩展包的工具； `av` （PyAV）是 FFmpeg 的 Python 绑定，主要用于音视频编解码链路。
- 你的目标如果是“飞书文本机器人接入”，可以先不装 `.[all]` ，走最小可用安装：

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码cd ~/hermes-agent
./venv/bin/python -m pip install -U pip setuptools wheel -i https://pypi.org/simple
./venv/bin/python -m pip install -e "." -i https://pypi.org/simple
# 飞书官方 extra 为 [feishu]（含 lark-oapi）；推荐写 .[feishu]，与源码 pyproject 一致
./venv/bin/python -m pip install -e ".[feishu]" -i https://pypi.org/simple
./venv/bin/python -m hermes_cli.main --version
```

若 `.[feishu]` 仍报网络问题，可临时改为手动： `pip install lark-oapi` （飞书 SDK；其余依赖一般已随 `pip install -e "."` 满足）。

- 等文本链路跑通后，如需语音/视频能力，再单独处理 `av/cython` 。

第三步：配置模型与 API Key

BASH📋 复制

```csharp
csharp 体验AI代码助手 代码解读复制代码# 方式 A：交互式配置（推荐；与 Installation Step 9 一致）
hermes model

# 方式 B：只写密钥（以 OpenRouter 为例；API Key 会进 ~/.hermes/.env，见 Configuration 文档）
hermes config set OPENROUTER_API_KEY "sk-or-v1-xxxxxxxxxxxxxxxx"

# 方式 C：阿里云通义 / DashScope（与 AI Providers 文档「Alibaba Cloud」表及示例一致）
# 密钥环境变量应为 DASHSCOPE_API_KEY（不是 OpenRouter 的 sk-or-）；CLI 单次验证示例：
#   hermes chat --provider alibaba --model qwen3.5-plus
hermes config set model.provider alibaba
hermes config set model.default qwen3.5-plus
hermes config set DASHSCOPE_API_KEY "你的DashScope密钥"
# Base URL：文档允许用 DASHSCOPE_BASE_URL 覆盖默认端点；请写入 ~/.hermes/.env（与文档「环境变量」表述一致）
# echo 'DASHSCOPE_BASE_URL=https://coding.dashscope.aliyuncs.com/v1' >> ~/.hermes/.env

# 方式 D（官方标注为 legacy，仅作迁移对照）：\`.env\` 里仅依赖 OPENAI_BASE_URL 做路由的做法已弃用
#（见 AI Providers「Legacy env vars」：OPENAI_BASE_URL 不再作为端点解析的信任源，应以 config.yaml / hermes model 为准）。
# 新安装请优先用方式 C，勿再以 OPENAI_* 作为 DashScope 主路径。
```

预期结果：

- `hermes model` 可完成 provider/model 选择（与官方 CLI 一致）
- 或 `hermes config set` 执行成功；Configuration 文档说明： **密钥进 `.env` ，其余非敏感项进 `config.yaml`**

补充（与 Configuration 一致）：也可用官方示例形式一次性写主模型，例如

`hermes config set model anthropic/claude-opus-4` （具体 slug 以你选用的提供商为准）。

失败分支：

- 如果提示 key 无效，检查是否有前后空格、是否使用了正确 provider 的 key
- 如果配置后不生效，重开终端并执行 `hermes status` 复核

**（可选读）不配 OpenRouter 时，辅助能力怎么接？**

官方 **AI Providers** 写明： **vision、网页摘要等侧路任务** 会用 **Auxiliary Models** ；在 `provider: "auto"` 时，链路会尝试 **OpenRouter → Nous → Codex** 等，所以 **最省事** 仍是配置 **`OPENROUTER_API_KEY`** 。

若你 **坚持不设 OpenRouter** ，又不想辅助调用失败，请在 **`~/.hermes/config.yaml`** 里按官方 [Configuration → Auxiliary Models（英）](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2Fuser-guide%2Fconfiguration%23auxiliary-models "https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auxiliary-models") / [配置说明 → 辅助模型（中）](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2Fuser-guide%2Fconfiguration "https://hermes-doc.aigc.green/user-guide/configuration") 给各槽位显式指定提供商与模型，例如：

- 将 **`auxiliary.vision`** 、 **`auxiliary.web_extract`** （及你实际会用的其它 `auxiliary.*` ）的 `provider` 设为 **`alibaba`** （配合已有 **`DASHSCOPE_API_KEY`** ），或设为 **`main`** 让辅助任务跟随当前主模型端点（须保证该端点支持对应多模态/文本能力）。
- **上下文压缩** 不走 `auxiliary.compression` 主块，而在顶层 **`compression:`** 里配置 **`summary_provider` / `summary_model` / `summary_base_url`** （同一 Configuration 文档「Context Compression」）。

修改后执行 **`hermes doctor`** 或 **`hermes config check`** 复核。

第四步：验证配置

BASH📋 复制

```
css 体验AI代码助手 代码解读复制代码hermes status
# 单次非交互提问：-q 与 --query 等价（Hermes chat 子命令定义如此）
hermes chat -q "请只回答数字：1+1 等于几？"
# 等价写法：hermes chat --query "请只回答数字：1+1 等于几？"
# 注意：若要「只输出最终结果、少横幅」，聊天里是大写 -Q / --quiet，不要和小写 -q（query）搞混
```

预期结果：

- `hermes status` 能看到当前 provider / model
- `hermes chat` 能返回模型回答（不要求固定措辞）

失败分支：

- 如果出现鉴权失败，回到第三步重新设置 key
- 如果超时或限流，先降低请求频率并重试
- 如果 CLI 正常但聊天失败，先用更短提示词验证链路再扩大任务

我踩的坑：

- API Key 末尾多空格，导致鉴权失败
- 配置完未重开 shell，导致 `hermes` 命令找不到
- Ubuntu 下 venv 缺 pip/依赖不全，导致 CLI 启动失败
- 建议先跑 `hermes doctor` ，异常时按上面的兜底流程补依赖

---

常见问题排查（安装阶段）

问题 1： `hermes` 命令找不到

表现：终端提示 `command not found`

排查：

1. 先执行 `source ~/.bashrc` （或你当前 shell 的配置文件）
2. 重开终端后重试 `hermes version`
3. 再跑一次 `hermes doctor`

问题 2：报 `No module named 'yaml'` 或 `No module named 'dotenv'`

表现：CLI 启动时报缺包

排查：

1. 进入项目目录： `cd ~/hermes-agent` （或你的实际路径）
2. 补基础依赖：`./venv/bin/python -m pip install pyyaml python-dotenv`
3. 再执行：`./venv/bin/python -m hermes_cli.main --version`

问题 3： `pip install -e ".[all]"` 报 `av/cython` 相关错误

表现：安装 `.[all]` 失败，提示构建 `av` 失败或找不到 `cython`

原因说明：

1\. `cython` 是构建部分 C 扩展包的工具

2\. `av` （PyAV）是 FFmpeg 的 Python 绑定，偏音视频能力

1. 这是可选多媒体能力，不等于 Hermes 主体不可用

排查（飞书文本接入优先）：

1. 先改用最小可用安装：`./venv/bin/python -m pip install -e "." -i https://pypi.org/simple`
2. 补飞书依赖：`./venv/bin/python -m pip install -e ".[feishu]" -i https://pypi.org/simple` （或仅 `pip install lark-oapi` ）
3. 验证：`./venv/bin/python -m hermes_cli.main --version`

---

飞书接入实战复盘（真实踩坑时间线 + 命令）

官方对网关命令、 `journalctl` 、允许列表与 **`GATEWAY_ALLOW_ALL_USERS`** 的说明见 [Messaging Gateway（英）](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-agent.nousresearch.com%2Fdocs%2Fuser-guide%2Fmessaging "https://hermes-agent.nousresearch.com/docs/user-guide/messaging") / [消息网关（中）](https://link.juejin.cn/?target=https%3A%2F%2Fhermes-doc.aigc.green%2Fuser-guide%2Fmessaging "https://hermes-doc.aigc.green/user-guide/messaging") ；飞书在文档中的工具集名为 **`hermes-feishu`** （与本地 `pip install -e ".[feishu]"` / `.[all]` 一致）。

这一节是我和读者实操时，按时间顺序踩过的坑。你可以直接当“故障手册”用。

#### 阶段 A：安装脚本跑了，但 CLI 不可用

现象：

- `No module named 'yaml'`
- `No module named 'dotenv'`
- `No module named pip`

处理命令：

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码cd ~/hermes-agent
./venv/bin/python -m ensurepip --upgrade
./venv/bin/python -m pip install -U pip setuptools wheel
./venv/bin/python -m pip install pyyaml python-dotenv
./venv/bin/python -m hermes_cli.main --version
```

结论：

- Ubuntu/venv 场景下，先确保 `pip` 和基础包齐全，再谈 gateway。

#### 阶段 B：.\[all\] 安装失败（av/cython）

现象：

- `Failed to build 'av'`
- `No matching distribution found for cython`

处理策略：

- 目标是“先跑飞书文本机器人”，可以不强依赖 `.[all]` 。
- 先走最小可用安装，后续再补音视频能力。

处理命令：

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码cd ~/hermes-agent
./venv/bin/python -m pip install -e "." -i https://pypi.org/simple
./venv/bin/python -m pip install -e ".[feishu]" -i https://pypi.org/simple
./venv/bin/python -m hermes_cli.main --version
```

#### 阶段 C：飞书不回复，但网关显示运行中

现象：

- `hermes gateway status` 显示网关已在运行（具体文案因版本略有差异）
- 飞书发消息没回

关键排查（ **先看你是哪种启动方式** ）：

1\. **若已执行过 `hermes gateway install` （Linux 用户级 systemd）** ：服务单元默认名为 `hermes-gateway` （使用 `HERMES_HOME` 多 profile 时可能是 `hermes-gateway-` ），可看日志：

`` ` `` bash

journalctl --user -u hermes-gateway -f

`` ` ``

不确定单元名时： `systemctl --user list-units 'hermes-gateway*'`

2\. **若是前台 `hermes gateway` / `hermes gateway run`** ：日志就在当前终端， **没有** 上述 `journalctl` 输出是正常的。

真实原因（常见）：

- 不是“进程没起”，而是 **用户白名单 / 私聊配对** 策略拦截（文档默认： **不在 allowlist 又未配对的用户会被拒绝** ）。
- 日志里可能出现与 allowlist 相关的提示。

更贴合官方、可长期用的做法（见 Messaging 文档「安全性 / 私聊配对」）：

- 在 `~/.hermes/.env` 中配置 **`FEISHU_ALLOWED_USERS`** （飞书用户 ID，逗号分隔），或
- 用户在机器人私聊里拿到 pairing code 后，在主控机执行： `hermes pairing approve feishu <配对码>` （平台名与源码 `Platform.FEISHU` 一致为 `feishu` ）。

快速验证（临时放开所有人； **仅测试，生产请改回白名单或配对** ）：

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码# 推荐（写入 ~/.hermes/.env，且避免反复 echo 追加重复行）
hermes config set GATEWAY_ALLOW_ALL_USERS true

cd ~/hermes-agent
# 若走 systemd 用户服务：
./venv/bin/python -m hermes_cli.main gateway restart
# 若你是前台跑的：先 Ctrl+C 停掉再执行
# ./venv/bin/python -m hermes_cli.main gateway
```

补充：

- `No home channel is set for Feishu` 一般不是“崩溃”，而是提醒：可在与机器人的会话里用 `/sethome` 绑定主会话（Hermes 帮助里会有说明）。

#### 阶段 D：飞书通了，但模型 401

现象：

- 飞书里出现： `Error code: 401`
- 日志里出现： `Missing Authentication header`
- 并且出现 `Failed to fetch model metadata from OpenRouter`

这类报错 99% 是“模型路由错了”，不是飞书问题。

我最终稳定可用的做法（与 **AI Providers** 对齐）：

- 使用官方一等提供商 **`alibaba`** + **`DASHSCOPE_API_KEY`** ，必要时用 **`DASHSCOPE_BASE_URL`** 指向你要的兼容端点
- 在 **`config.yaml`** 中固定 `model.provider` / `model.default` ，避免路由飘到 OpenRouter
- **慎删** `OPENROUTER_API_KEY` ：官方 **AI Providers** 注明，即便主模型不用 OpenRouter， **vision / web 摘要等辅助能力** 默认仍可能依赖 OpenRouter；若删除后辅助工具异常，请改配 `configuration` 中的 **Auxiliary Models** 或恢复密钥

处理命令（示例； **请把密钥换成你自己的** ，勿粘贴真实 Key 到文章/外部）：

BASH📋 复制

```bash
bash 体验AI代码助手 代码解读复制代码cd ~/hermes-agent

# 若确需去掉 OpenRouter（并接受辅助能力可能受限），再执行删除；否则可跳过本段。
# 注意：复制到终端时，sed 的参数必须是「一对完整单引号」包住正则；macOS 需 sed -i '' '...'；Linux 为 sed -i '...'。
# 去掉下面两行开头的 # 再执行（整行复制，勿缺末尾引号）：
# sed -i '/^OPENROUTER_API_KEY=/d' ~/.hermes/.env
# sed -i '/^OPENROUTER_BASE_URL=/d' ~/.hermes/.env

# 推荐：DashScope 首选环境变量名（见 AI Providers 表格）
hermes config set model.provider alibaba
hermes config set model.default qwen3.5-plus
hermes config set DASHSCOPE_API_KEY "你的DashScope密钥"

# Base URL 覆盖：写入 ~/.hermes/.env（与文档中 DASHSCOPE_BASE_URL 说明一致；具体 URL 以阿里云控制台为准）
sed -i '/^DASHSCOPE_BASE_URL=/d' ~/.hermes/.env
echo 'DASHSCOPE_BASE_URL=https://coding.dashscope.aliyuncs.com/v1' >> ~/.hermes/.env

# 可选清理：避免 legacy OPENAI_* 与文档推荐路径混用（AI Providers 已说明 OPENAI_BASE_URL 不再用于端点解析）
sed -i '/^OPENAI_BASE_URL=/d' ~/.hermes/.env

# 重启网关（Hermes 0.7.x：\`gateway start\` / \`stop\` / \`restart\` 均为合法子命令）
./venv/bin/python -m hermes_cli.main gateway stop
./venv/bin/python -m hermes_cli.main gateway start
#
# 若你已把 venv/bin/hermes 加入 PATH，可与上文等价：
# hermes gateway stop && hermes gateway start
#
# 若确定是用 systemd --user 安装的默认单元 hermes-gateway，也可：
# systemctl --user restart hermes-gateway
```

上文 `hermes config set model.*` 已写入 **`config.yaml`** （Configuration 文档： **非密钥项以该文件为主要信任源** ；密钥仍在 `.env` ）。模型 ID **以 DashScope / 控制台为准** 。最后用 `hermes status` 、 `hermes chat --provider alibaba --model <你的模型>` 或 `hermes doctor` 复核。

验证标准：

- 飞书发“你好”有自然语言回复
- 日志里不再出现 OpenRouter 401 报错

一句话总结这次飞书实战：

- **装了 systemd 用户服务时** 通道问题优先 `journalctl --user -u hermes-gateway` ；前台运行则看终端
- 模型问题看 `401` 和请求打到的 `Endpoint`
- 不要把“网关运行中”误判为“链路全通”

---

下篇预告（实战篇）

安装跑通后，下一篇我会带你做一个真实测试场景：

- 场景：登录接口回归测试
- 目标：从任务拆解到测试报告，一次走通
- 输出：可复用提示词模板 + 结构化报告模板 + 发布建议模板

如果你已经跑通安装，留言告诉我你卡过的报错关键词（比如 `dotenv` 、 `av` 、 `gateway` ），我会在实战篇里把这些坑一起覆盖。

---

> 如果你也在接 Hermes + 飞书，评论区回我你卡住的报错关键词（例如 `yaml` 、 `401` 、 `gateway` ），我会把高频问题整理成一张“速查表”发下一篇。

你现在卡在哪一步？留言区回我一个关键词（ `安装` / `飞书不回` / `401` ），我按留言数量先更哪篇排障。

看完先做一件事：先跑 `hermes doctor` ，再回评论区告诉我你卡在哪一步。