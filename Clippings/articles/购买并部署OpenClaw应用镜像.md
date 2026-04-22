---
title: "购买并部署OpenClaw应用镜像"
source: "https://help.aliyun.com/zh/simple-application-server/use-cases/quickly-deploy-and-use-openclaw?spm=a2c4g.11186623.0.i1"
author:
published:
created: 2026-04-22
description: "OpenClaw是一款开源的本地优先AI代理与自动化平台。可通过OpenClaw将多渠道通信能力与大语言模型深度集成，创建拥有持久记忆与主动执行能力的定制化 AI 助理。"
tags:
  - "clippings"
---
**OpenClaw是一款开源的本地优先AI代理与自动化平台** 。可通过OpenClaw将多渠道通信能力与大语言模型深度集成，创建拥有持久记忆与主动执行能力的定制化 AI 助理。

**重要**

OpenClaw 为开源 AI 助手，请在使用前充分评估其安全性与稳定性并严格遵循许可协议， **以切实保障系统环境与数据安全。**

## 计费说明

在轻量应用服务器上部署并使用OpenClaw服务将产生以下费用：

- **轻量应用服务器费用：** 参见 [轻量应用服务器计费概述](https://help.aliyun.com/zh/simple-application-server/product-overview/overview) 。
- **模型调用费用：** OpenClaw执行过程中默认调用百炼模型。模型调用的主要计费方式有两种：
	- [Coding Plan](https://help.aliyun.com/zh/model-studio/coding-plan) **AI 编码套餐（推荐）：** 采用固定月费模式，提供月度请求额度，超出时段限额的调用会报错且不计费用，可避免产生超出预期的费用。
		> Coding Plan 目前支持 `qwen3.5-plus` 、 `kimi-k2.5` 、 `MiniMax-M2.5` 、 `glm-5` 等模型，详细的模型列表请参考 [Coding Plan概述](https://help.aliyun.com/zh/model-studio/coding-plan#dc0d98da6ev4j) 。
		- **按Token用量计费：** `OpenClaw 2026.2.26` 及以上版本：默认使用 `qwen3.5-plus` 模型作为文本和图像处理模型，计费详见 [千问Plus](https://help.aliyun.com/zh/model-studio/model-pricing#baa85ffef6dyz) 。
		> 其他版本的默认模型以及计费详见。
		**重要**
		**配置免费额度用完即停** ：首次开通阿里云百炼时，会自动发放各模型的 [新人免费额度](https://help.aliyun.com/zh/model-studio/new-free-quota#70f9e8874acq1) 。免费额度消耗完后，默认将按 [模型列表](https://help.aliyun.com/zh/model-studio/models) 中的价格与用量计费，建议开启 [免费额度用完即停](https://help.aliyun.com/zh/model-studio/new-free-quota#d1cb80ac11i92) 功能，避免产生额外费用。更多计费问题可参见 [OpenClaw（原MoltBot、Clawbot）购买与费用问题](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-faq#94ab1251f8wk2) 。

## 购买OpenClaw套餐

**重要**

如果已购买轻量应用服务器，可以跳过此步骤，以重置系统的方式部署OpenClaw（重置系统时选择应用镜像下的OpenClaw镜像），但重置系统会清除轻量应用服务器上的系统盘数据，请根据需要做好数据备份。具体操作，请参见 [重置系统](https://help.aliyun.com/zh/simple-application-server/user-guide/reset-a-simple-application-server) 。如需保留AI助理的记忆、身份配置和Skills等工作区数据，请参见 [升级OpenClaw版本的数据备份与恢复](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-upgrade-data-backup-restore) 。

1. [购买预装OpenClaw应用的轻量应用服务器](https://swasnext.console.aliyun.com/buy?regionId=cn-beijing&planId=swas.s.c2m2s40b1.linux&imageId=39befe1037bc41a7856ca8ca639d7948&amount=1&duration=12&autoRenew=false#/) 。
2. 在 **轻量应用服务器** 页面，预置了资源配置，如要更改配置项，请参考下面内容。
	- **实例** ：内存必须2GiB及以上，可以根据自己的需求切换套餐。
		- **地域** ：默认 **北京** 。
		- **购买配置** ：默认12个月，可以根据自己的需求切换时长。

## 配置OpenClaw

1. 在 [轻量应用服务器-控制台](https://swasnext.console.aliyun.com/servers) ，单击服务器卡片中的实例ID，在 **服务器概览** 页面单击 **应用详情** 页签。
2. 在 **OpenClaw使用步骤** 区域中，单击 **端口放通** 下的 **执行命令** ，可开放获取OpenClaw服务运行端口的防火墙。
	**重要**
	- 为了防止恶意扫描与定向攻击，OpenClaw 在初始化时不再使用固定的默认端口，而是自动生成一个随机端口，可在控制台。
	- 端口放通将使服务暴露于公网，支持一键关闭 WebUI 公网访问，详见
3. 单击 **配置OpenClaw** 下的 **执行命令** 配置百炼API key。
	目前支持配置两种类型的百炼API Key：
	- [Coding Plan](https://help.aliyun.com/zh/model-studio/coding-plan) **套餐专属 API Key（推荐）：** 采用固定月费模式，提供月度请求额度，超出时段限额的调用会报错且不计费用，可避免产生超出预期的费用。
		> Coding Plan 目前支持 `qwen3.5-plus` 、 `kimi-k2.5` 、 `MiniMax-M2.5` 、 `glm-5` 等模型，详细的模型列表请参考 [Coding Plan概述](https://help.aliyun.com/zh/model-studio/coding-plan#dc0d98da6ev4j) 。
		- **按Token用量计费的百炼API Key。**
	配置API Key。在下拉框中选择Coding Plan的API Key或直接输入按量计费的API Key，选择模型后单击 **下一步** 。
	> 手动输入API Key时，需确保所选地域与API Key对应的地域一致，否则会导致模型无法正常调用。
4. 单击 **访问Web UI面板** 下的 **获取地址** ，获取OpenClaw WebUI的地址，可以在Web页面与OpenClaw的Agent对话。
	> 可根据需求参考一键关闭WebUI的公网访问权限。
5. （可选）查看Token。
	在 **应用详情** > **基础配置** > **查看Token** 中单击 **查看** ，查看并保存Token。
	**警告**
	请勿泄露包含 Token 的完整 URL。该链接包含身份验证凭据， **任何持有此链接的人都能直接绕过登录验证** ，获得 OpenClaw 控制台的管理员权限。

## 配置消息渠道

OpenClaw可以在聊天应用上与你交流。所有渠道都支持文本，图片、视频等消息的回复支持因渠道而异。阿里云为您在轻量应用服务器控制台的应用详情界面上提供了钉钉、飞书、微信、企业微信、QQ消息渠道的快速接入通道，可参考以下文档进行配置。

- [OpenClaw集成钉钉](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-integrated-dingtalk)
- [OpenClaw集成飞书](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-integrated-fly-book)
- [OpenClaw集成微信](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-integrated-wechat#wx01title82kf9)
- [OpenClaw企业微信集成](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-enterprise-wechat-integration)
- [OpenClaw集成QQ](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-qq-integration)
- [OpenClaw Web页面集成](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-web-page-integration)
- [通过OpenClaw调用iMessage](https://help.aliyun.com/zh/simple-application-server/use-cases/invoking-imessage-via-openclaw)

## OpenClaw个性化配置

通用Agent表现得“千人一面”，难以满足特定场景下的交互需求。为了让 OpenClaw 的 Agent 真正融入业务场景（如沉浸式角色扮演、严谨的企业客服等），OpenClaw 提供了 **个性化配置能力** 。阿里云为您提供了部分场景配置示例，可参见 [OpenClaw 个性化配置模板与场景示例](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-personalized-configuration-template-and-scenario-example) 进行配置。

**具体配置文件包括** ：

- **性格定义（** [**SOUL.md**](https://docs.openclaw.ai/reference/templates/SOUL) **）** ：定义 AI 的核心价值观、对话风格（如严肃、幽默、简洁）以及行为准则。
- **身份定义（** [**IDENTITY.md**](https://docs.openclaw.ai/reference/templates/IDENTITY) **）** ：定义 AI 的姓名、自我认知、背景设定以及角色定位。
- **工作方式定义（** [**AGENTS.md**](https://docs.openclaw.ai/reference/templates/AGENTS) **）** ：定义 AI 处理任务的逻辑、工具使用规则以及工作流。

**配置步骤：** 在 **应用详情** > **个性化配置** 中单击 **编辑** 修改不同的配置文件。具体场景化配置示例可参考： [OpenClaw 个性化配置模板与场景示例](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-personalized-configuration-template-and-scenario-example#69698fa40c7e7) 。

## 常见问题

### 如何重启OpenClaw网关？

当遇到连接中断或服务不可用等场景时，可在控制台页面重启OpenClaw网关。在 **应用详情** > **基础配置** > **重启OpenClaw网关** 中单击 **执行命令** 。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0611033771/p1058999.png)

### 如何查看OpenClaw的端口号？

为了防止恶意扫描与定向攻击，OpenClaw 在初始化时不再使用固定的默认端口，而是自动生成一个 **随机端口** 。在 **应用详情** > **基础配置** > **查看端口** 中单击 **执行命令** 查看OpenClaw的端口号。

### 如何更改OpenClaw调用的模型？

OpenClaw集成了阿里云百炼平台，在页面切换不同的模型。在 **应用详情** > **模型配置** > **模型配置** 中删除默认的模型，然后下拉选择不同的百炼模型。

> 支持手动输入模型名，模型Code可以在 [百炼模型广场](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/all) 页面查询。

### 如何开启/关闭OpenClaw WebUI的公网访问？

用户可根据自身需求一键关闭OpenClaw WebUI的公网访问权限。在 **应用详情** > **基础配置** > **公网访问** 中单击 **开启/关闭** 控制OpenClaw WebUI的公网访问能力。

### 为什么填写API Key时系统不识别我已有的百炼API Key？

系统会自动检测离当前服务器所在地域最近的百炼模型接入点，并展示其对应的API Key（如果订阅了百炼Coding Plan，会同时展示其API Key）。如果不存在就近接入点对应的API Key，可按界面操作在对应的地域创建API Key或订阅Coding Plan。

<table><tbody><tr><td rowspan="1" colspan="1"><p><b>轻量应用服务器所在地域</b></p></td><td rowspan="1" colspan="1"><p><b>系统推荐的百炼API Key对应地域</b></p></td><td rowspan="1" colspan="1"><p><b>Coding Plan的API key对应地域</b></p></td></tr><tr><td rowspan="1" colspan="1"><p>中国内地地域</p></td><td rowspan="1" colspan="1"><p>华北2（北京）</p></td><td rowspan="3" colspan="1"><p>华北2（北京）</p></td></tr><tr><td rowspan="1" colspan="1"><p>美国及欧洲地域</p></td><td rowspan="1" colspan="1"><p>美国（弗吉尼亚）</p></td></tr><tr><td rowspan="1" colspan="1"><p>中国香港及其他亚洲地域</p></td><td rowspan="1" colspan="1"><p>新加坡</p></td></tr></tbody></table>

### 为什么我的OpenClaw的默认模型不是qwen3.5-plus？

目前只有最新的镜像版本 `OpenClaw 2026.2.26` 默认使用 `qwen3.5-plus` 模型。其他版本的默认模型如下：

- `OpenClaw 2026.2.3` 和 `OpenClaw 2026.2.9` 版本：默认使用 `qwen3-max-2026-01-23` 模型作为文本处理模型（Primary Model）， `qwen3-vl-plus` 模型作为图像处理模型（Image Model），计费详见 [千问Max](https://help.aliyun.com/zh/model-studio/model-pricing#c3741fefddnzj) 、 [千问VL](https://help.aliyun.com/zh/model-studio/model-pricing#499d0324a8dex) 。
- `OpenClaw(Moltbot) 2026.1.27-beta.1` 版本：2026年1月31日及之后购买的服务器默认使用 `qwen3-max-2026-01-23` 模型，2026年1月31日之前默认使用 `qwen-vl-plus` 模型。

如需更换模型可手动。

## 相关文档

- [OpenClaw应用镜像发布记录](https://help.aliyun.com/zh/simple-application-server/use-cases/update-log-of-openclaw-image)
- [OpenClaw 常见问题](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-faq)