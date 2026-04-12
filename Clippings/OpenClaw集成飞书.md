---
title: "OpenClaw集成飞书"
source: "https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-integrated-fly-book?spm=a2c4g.11186623.help-menu-58607.d_3_0_0_2.806f66eeYESGS0"
author:
published:
created: 2026-04-12
description: "本文介绍将 OpenClaw服务与飞书集成，实现在飞书群聊或单聊中，通过自然语言直接与OpenClaw交互。"
tags:
  - "clippings"
---
本文介绍将 OpenClaw服务与飞书集成，实现在飞书群聊或单聊中，通过自然语言直接与OpenClaw交互。

## 环境准备

配置消息渠道前，需参考以下步骤或 [部署OpenClaw镜像](https://help.aliyun.com/zh/simple-application-server/use-cases/quickly-deploy-and-use-openclaw) 文档购买并配置OpenClaw应用镜像的轻量应用服务器，若已完成可跳过此步骤。

**购买并配置OpenClaw应用镜像的轻量应用服务器**

### 步骤一、购买OpenClaw套餐

**重要**

如果已购买轻量应用服务器，可以跳过此步骤，以重置系统的方式部署OpenClaw（重置系统时选择应用镜像下的OpenClaw镜像），但重置系统会清除轻量应用服务器上的系统盘数据，请根据需要做好数据备份。具体操作，请参见 [重置系统](https://help.aliyun.com/zh/simple-application-server/user-guide/reset-a-simple-application-server) 。

1. [购买预装OpenClaw应用的轻量应用服务器](https://swasnext.console.aliyun.com/buy?regionId=cn-beijing&planId=swas.s.c2m2s40b1.linux&imageId=6b04ab451cc94a1b8a13876eabf64e8b&amount=1&duration=12&autoRenew=false#/) 。
2. 在 **轻量应用服务器** 页面，预置了资源配置，如要更改配置项，请参考下面内容。
	- **实例** ：内存必须2GiB及以上，可以根据自己的需求切换套餐。
		- **地域** ：默认 **北京** 。
		- **购买配置** ：默认12个月，可以根据自己的需求切换时长。

### 步骤二、配置OpenClaw

1. 在 [轻量应用服务器-控制台](https://swasnext.console.aliyun.com/servers) ，单击服务器卡片中的实例ID，在 **服务器概览** 页面单击 **应用详情** 页签。
2. 在 **OpenClaw使用步骤** 区域中，单击 **端口放通** 下的 **执行命令** ，可开放获取OpenClaw服务运行端口的防火墙。
	**重要**
	- 为了防止恶意扫描与定向攻击，OpenClaw 在初始化时不再使用固定的默认端口，而是自动生成一个随机端口，可在控制台 [查看OpenClaw的端口号](https://help.aliyun.com/zh/simple-application-server/use-cases/quickly-deploy-and-use-openclaw#e6598c42c3ou0) 。
	- 端口放通将使服务暴露于公网，支持一键关闭 WebUI 公网访问，详见 [如何开启/关闭OpenClaw WebUI的公网访问？](https://help.aliyun.com/zh/simple-application-server/use-cases/quickly-deploy-and-use-openclaw#836078a415vme)
3. 单击 **配置OpenClaw** 下的 **执行命令** 配置百炼API key。
	目前支持配置两种类型的百炼API Key：
	- [Coding Plan](https://help.aliyun.com/zh/model-studio/coding-plan) **套餐专属 API Key（推荐）：** 采用固定月费模式，提供月度请求额度，超出时段限额的调用会报错且不计费用，可避免产生超出预期的费用。
		> Coding Plan 目前支持 `qwen3.5-plus` 、 `kimi-k2.5` 、 `MiniMax-M2.5` 、 `glm-5` 等模型，详细的模型列表请参考 [Coding Plan概述](https://help.aliyun.com/zh/model-studio/coding-plan#dc0d98da6ev4j) 。
		- **按Token用量计费的百炼API Key。**
	API Key配置方式包括 **系统推荐** 及 **手动输入** 。系统推荐会列出百炼Coding Plan的API Key（成本可控），及离服务器最近的百炼模型服务的API Key（时延较低）。若需使用其他地域或者其他账号的API Key可选择 **手动输入。**
	- **系统推荐（下拉选择）**
		选择完成后单击 **下一步** 。
		<table><tbody><tr><td rowspan="1" colspan="1"><p><b>轻量应用服务器所在地域</b></p></td><td rowspan="1" colspan="1"><p><b>系统推荐的百炼API Key对应地域</b></p></td><td rowspan="1" colspan="1"><p><b>Coding Plan的API key对应地域</b></p></td></tr><tr><td rowspan="1" colspan="1"><p>中国内地地域</p></td><td rowspan="1" colspan="1"><p>华北2（北京）</p></td><td rowspan="3" colspan="1"><p>华北2（北京）</p></td></tr><tr><td rowspan="1" colspan="1"><p>美国及欧洲地域</p></td><td rowspan="1" colspan="1"><p>美国（弗吉尼亚）</p></td></tr><tr><td rowspan="1" colspan="1"><p>中国香港及其他亚洲地域</p></td><td rowspan="1" colspan="1"><p>新加坡</p></td></tr></tbody></table>
		- **手动输入**
		单击按钮切换至手动输入，输入百炼API Key并选择该API Key对应地域，单击 **下一步** 。 ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1942220771/p1052681.png)
		**重要**
		手动配置需确保选择的API Key对应地域正确，否则会导致模型无法正常调用。
4. 单击 **访问Web UI面板** 下的 **获取地址** ，获取OpenClaw WebUI的地址，可以在Web页面与OpenClaw的Agent对话。
	> 可根据需求参考 [关闭OpenClaw WebUI的公网访问](https://help.aliyun.com/zh/simple-application-server/use-cases/quickly-deploy-and-use-openclaw#836078a415vme) 一键关闭WebUI的公网访问权限。
5. （可选）查看Token。
	在 **应用详情** > **基础配置** > **查看Token** 中单击 **查看** ，查看并保存Token。
	**警告**
	请勿泄露包含 Token 的完整 URL。该链接包含身份验证凭据， **任何持有此链接的人都能直接绕过登录验证** ，获得 OpenClaw 控制台的管理员权限。

## 集成飞书

> OpenClaw插件集成方式仅支持镜像版本为 `OpenClaw 2026.2.9` 及以上的实例。如需在旧版本中集成该消息渠道，请参考 [通过AppFlow集成消息渠道](https://help.aliyun.com/zh/simple-application-server/use-cases/integrate-message-channels-through-appflow) 。您可在轻量应用服务器概览页的 **基本信息** > **镜像信息** 中查看当前实例的镜像版本。

控制台扫码接入

手动配置

> 只支持 OpenClaw 2026.3.28 镜像及以上版本，其他版本使用手动配置接入。

1. 登录 [轻量应用服务器控制台](https://swasnext.console.aliyun.com/servers/) ，找到目标 OpenClaw 服务器，进入 **应用详情** 页签。
2. 在 **通道配置** 区域的 **飞书** 部分，单击 **扫码配置** 。
3. 等待命令执行完成后，页面将显示一个二维码。使用飞书扫描该二维码完成接入。
	> 生成二维码一般需要30秒到2分钟，请耐心等待。
4. 扫码完成后，单击 **关闭** 。
5. 与机器人对话验证。
	> 首次对话一般需要等待30秒到2分钟，请耐心等待。

### 1\. 创建飞书应用

1. 访问 [飞书开放平台](https://open.feishu.cn/app) ，单击 **创建企业自建应用** ，填写应用名称和描述，选择应用图标，单击 **创建** 。
2. 左侧导航栏单击 **凭证与基础信息** 页面，复制 **App ID** （格式如 `cli_xxx` ）和 **App Secret** 。
3. 左侧导航栏单击 **权限管理** 页面，点击 **批量导入/导出权限** 按钮，粘贴以下 JSON 配置，单击 **下一步，确认新增权限** ，单击 **申请开通** 。
	**JSON配置文件内容**
	```bash
	{
	  "scopes": {
	    "tenant": [
	      "aily:file:read",
	      "aily:file:write",
	      "application:application.app_message_stats.overview:readonly",
	      "application:application:self_manage",
	      "application:bot.menu:write",
	      "cardkit:card:write",
	      "contact:user.employee_id:readonly",
	      "corehr:file:download",
	      "docs:document.content:read",
	      "event:ip_list",
	      "im:chat",
	      "im:chat.access_event.bot_p2p_chat:read",
	      "im:chat.members:bot_access",
	      "im:message",
	      "im:message.group_at_msg:readonly",
	      "im:message.group_msg",
	      "im:message.p2p_msg:readonly",
	      "im:message:readonly",
	      "im:message:send_as_bot",
	      "im:resource",
	      "sheets:spreadsheet",
	      "wiki:wiki:readonly"
	    ],
	    "user": ["aily:file:read", "aily:file:write", "im:chat.access_event.bot_p2p_chat:read"]
	  }
	}
	```
4. 左侧导航栏中单击 **添加应用能力** ， 选择 **按能力添加** 页签，找到 **机器人** 卡片，单击 **配置** 。
5. 配置事件订阅。
	1. 在 [轻量应用服务器控制台](https://swasnext.console.aliyun.com/servers) ，进入目标实例详情页，在 **应用详情** > **通道配置** > **飞书** 区域，填入，并单击 **应用** 。
		2. 在飞书开放平台左侧导航栏单击 **事件与回调** ，在 **事件配置** 页签中单击 **订阅方式** ，选择 **使用 长连接 接收事件** ，单击 **保存** 。
		3. 在事件配置页面，单击 **添加事件** ，搜索事件 `im.message.receive_v1` （接收消息），单击 **确认添加** 。
6. 在 **版本管理与发布** 页面创建版本，填写 **应用版本号** 和 **更新说明** ，单击 **保存** ，提交审核并发布。

### 2\. 配置机器人

可以创建群聊或在已有群聊中添加机器人，在飞书群中 **@机器人** 进行对话，或通过搜索的方式与机器人私聊进行测试。

> 若需在外部群中使用机器人，可参考配置文档 [机器人支持外部群和外部用户单聊](https://open.feishu.cn/document/develop-robots/add-bot-to-external-group) 。

1. 按照添加路径添加机器人： **···** > **设置** > **群机器人** > **添加机器人** 。
2. 单击机器人头像，单击发送消息，可向机器人私发一条消息，@机器人可在群中向机器人发送消息。

> OpenClaw 2026.3.13 版本之前，需使用配对码连接机器人，可参考如下步骤配置。

**使用配对码连接机器人**

1. 向机器人私发消息，机器人会回复一个 **配对码** 。
2. 在WebUI页面输入 `openclaw pairing approve feishu 配对码` 完成配对。
	> 配对码是上一步机器人回复的配对码。
	**重要**
	如出现“目前没有待处理的配对请求”报错，请参考。

## 常见问题

### 如何通过终端命令将OpenClaw与飞书配对？

1. 登录服务器。
	1. 登录 [轻量应用服务器控制台](https://swasnext.console.aliyun.com/servers/) 。
		2. 在服务器列表中，找到目标服务器卡片，单击卡片中的 **远程连接** 。在弹出的连接窗口中，在 **Workbench 一键连接** 区域单击 **立即登录** 。
2. 获取配对码。
	在终端执行以下命令，找到待配对的飞书机器人配对码，复制查询结果中的配对码。
	```bash
	openclaw pairing list feishu
	```
3. 完成配对。
	在终端执行以下命令，批准配对请求。将命令中的YXXX替换为上一步获取的实际配对码。
	```
	openclaw pairing approve feishu YXXX
	```

### 如何配置OpenClaw定时执行任务并输出内容到飞书机器人？

可以通过与OpenClaw对话创建定时任务。

1. 获取群机器人的 **Webhook地址：**
	1. 单击群 **设置** > **群机器人** 。
		2. **单击** 添加机器人，选择自定义机器人。填写机器人名称和描述，单击 **添加** ，复制 **Webhook地址** 。
2. 在OpenClaw对话中创建相应任务，格式为定时任务内容+群机器人的Webhook地址，以查询实时天气为例创建定时任务。
3. 验证消息发送。可在对话中让Agent立即发送消息，测试该定时任务。在机器人所在的群聊查看是否执行定时任务。

> 如要修改或者取消定时任务，可直接在对话中让Agent修改或取消定时任务。

如需使用AppFlow配置定时任务，请参考 [如何使用AppFlow配置定时任务](https://help.aliyun.com/zh/simple-application-server/use-cases/openclaw-faq#d4184be05fem7) 。