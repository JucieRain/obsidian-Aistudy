---
title: "‍⁢⁣⁡‌⁣⁤﻿⁤​⁡‌⁤​⁣⁣﻿‬⁣​‌‌‌⁣​‍⁡‬⁣⁣​‬⁡​​​‌﻿⁡​⁤﻿‌⁡﻿​​﻿⁡﻿飞书云文档"
source: "https://bytedance.larkoffice.com/docx/WnHkdJQM6oGpQFxm9i7ckVdenSh"
author:
published:
created: 2026-04-12
description:
tags:
  - "clippings"
---
飞书 CLI 能力介绍与最佳实践

最近修改: 昨天 22:59

- [飞书 CLI 能力介绍与最佳实践](#WnHkdJQM6oGpQFxm9i7ckVdenSh)
- [等一下，CLI 是什么？跟我有什么关系？](#FDAfdxD7HoXTQfxmbEPcQ1gZnEb)
- [谁会用到它](#RU1Rddf2QoP98xxly2GchBLwnkc)
- [1\. 📦 快速安装](#C4rrdiphYoWpJOxOSc4cERCgnjd)
- [可选：快速完成用户授权](#FCR4dyoExo6fcqx2KTNcdRC7nhd)
- [🎉 开启我的第一个任务](#CJtFdlMovoysYuxnI8gcL5UPnMg)
- [2\. 🎬 能做什么](#NiTwdtzDWo48DHxun65c7u2Zntb)
- [场景 1：开完会，事就办了](#BdBQdal0lol85pxc6MKcfqeUnog)
- [场景 2：人与 AI 共创文档](#MpRIdA3cRoQnisx9csWcK1g6nIc)
- [场景 3：跨时区多人智能约会](#EIGAdEhKwoykWYxC2TXcGknQnRR)
- [场景 4：会议审计到多维表格仪表盘](#XerNdVBvcombE7xCAcHcJ2XTnsb)
- [场景 5：未读邮件智能分类与处理](#NrjndGPWRoToh2xpkLBc8LSrnye)
- [3\. 💗 为什么选择飞书 CLI](#UIRBd8uN6osx9rxP1fRcRQRynSh)
- [你的 AI 缺两样东西：context 和手](#XdIUd6fWzowCWexr7mwcJUHKnKb)
- [为 AI 而设计](#MFfPdSlBjohYLwxOrbFcafm3nkb)
- [全面开源，自由调用](#CE2Td8mKJoqwVlxisEBc2OfLnwb)
- [覆盖全，迭代快](#FZ1vdjs7poYG6KxidUNcuKwmnXY)
- [4\. 🧾 附录](#IxP2dX2iXodnrXxX6Bzcxgnbn4f)
- [认证与配置](#LtYidQsd7ojR33xIKHvcWEdRn6b)
- [各业务域核心能力](#HqDdd1b4foSIrlx9RGOc4wvjnQf)
- [5\. 🙋 常见问题](#N0qvd4bCFo4fwkxnQyJcfa8YnpC)
- [6\. 入群参与讨论、订阅后续更新](#FtA9dXun0oLb5BxivHFcisNPn6d)
- [7\. ⛲️许愿池](#D0fDdSgLLotuH7x8ArScx0TPnGh)
- [8\. 更新日志](#MlErd71y6oOzWUx6zX4cGU7rnHh)
- [V 1.0.4 更新](#Uiz2dEPUdogtu3xPJJzcovzAn08)
- [V 1.0.3 更新](#AiVddQxOroILBXx5L5zcRCbEnPd)

English Version： [Lark CLI: Let AI Actually Do Your Work in Lark](https://bytedance.larkoffice.com/wiki/P6DiwXsrZiMYBOk2ikzc9Btanee) （海外 Lark 已支持）

💫

飞书 CLI 正式开源，给每个 Agent 一双操作飞书的手

你的 AI Agent 很聪明，但它看不到你的日历，读不了你的群聊，打不开你的文档。它就像一个能力很强但没有手的人，只能跟你聊天，不能帮你干活。

飞书 CLI 就是给 Agent 的那双手。装上之后，你的 Agent 可以直接读你的飞书消息、查你的日历、写文档、建多维表格、搜知识库、发邮件。不是生成一段文字让你复制粘贴，而是直接在飞书里帮你把事情办了。

以前是你操作飞书，现在是 AI 操作飞书，你只管拍板。

零门槛，真开源

无需登记，无需审核。飞书 CLI 现已面向所有用户开源。我们相信，开源不应设置人为障碍。

无论你想让 Claude Code、Codex 还是其他 Agent 直接操作飞书，或是希望围绕飞书构建新一代自动化工作流，欢迎立即获取代码，即刻上手：👉 [\[GitHub 开源地址\]](https://github.com/larksuite/cli)

🦞 如果你是 OpenClaw、飞书 aily 用户：用户无需单独安装飞书 CLI。我们即将上线内置全部 CLI 能力的「飞书官方 OpenClaw 插件」、升级飞书 aily 能力，升级后即可无缝体验。

入群参与讨论、订阅后续更新

![](https://s1-imfile.feishucdn.com/static-resource/v1/v3_00107_cf651b6a-bc81-47ec-914d-d930e56cd61g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp)

【Bytedance】飞书 CLI 交流互助群 | Lark CLI Communication & Support

字节内部的飞书 CLI 交流互助

群名片

加入

加入

50%

![](https://s1-imfile.feishucdn.com/static-resource/v1/v3_00109_457eeaf5-5465-4076-b680-ee16d6b62ebg~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp)

飞书 CLI 交流互助群 ｜Lark CLI Communication & Support

外部

群名片

加入

加入

50%

等一下，CLI 是什么？跟我有什么关系？

你可能觉得 CLI（命令行工具）是程序员的东西，跟自己没关系。换个方式理解：

你跟 AI 的对话，其实不是两个人的私聊，而是一个三人群聊。

群里有三个人：你、AI、你的电脑（或者说飞书）。

•

你发消息 = 你在跟 AI 说话

•

AI 执行命令 = AI 在跟飞书说话

•

飞书返回结果 = 飞书在回复你们俩

以前的问题是：飞书没有加入这个群聊。AI 再聪明，它跟飞书之间没有沟通渠道，所以只能给你建议，不能帮你干活。

飞书 CLI 就是把飞书拉进了这个群聊。 装上之后，AI 终于能直接跟飞书对话了：帮你查日历、发消息、写文档、建表格。

所以 CLI 跟你的关系是：你完全不需要学它，甚至不需要知道它存在。 你只管用自然语言跟 AI 说话，AI 会自己用 CLI 去操作飞书。你只需要安装一次，之后就忘了它吧。

谁会用到它

•

使用 Trae、Claude Code、Codex、Cursor 等 AI 工具的用户

直接安装 CLI，让 AI 代你操作飞书——总结昨日工作、整理群聊消息、批量更新多维表格数据。一行命令完成安装，几分钟即可上手。

•

构建企业级 AI Agent 的团队

如果你正在开发需要与飞书深度集成的 AI 产品——无论是 AI 员工、AI 客服还是自动化工作流——CLI 提供飞书官方推荐的最佳实践，覆盖核心业务域的高频操作，同时支持用户身份与应用身份，可直接集成进你的 Agent。

•

使用 OpenClaw 的用户（敬请期待）

如果你在 OpenClaw 中安装了飞书插件，我们即将基于这套 CLI 能力升级插件底层。升级完成后，无需自行安装 CLI，直接用自然语言与 AI 对话即可操作飞书。

1.

📦 快速安装

19

2

8

1

4

5

评论（56）

跳转至首条评论

Yvon Shong3月29日 21:55

什么时候

王泽腾 Larkin3月30日 09:53

正在加紧开发中，晚线时间公布时间～

刘正义3月30日 10:49

期待期待，赶紧赶紧

长孙无限3月30日 11:26

哈哈，是说这个么 [OpenClaw 飞书官方插件使用指南（公开版）](https://bytedance.larkoffice.com/docx/MFK7dDFLFoVlOGxWCv5cTXKmnMh)

刘正义3月30日 11:27

这个还没集成 cli，催更集成

刘承川3月30日 15:49

已经手动让我的 claw 装了 cli 了，但是 claw 和 cli 是俩应用，现在有跨应用转换 id 的问题

牛晶泾3月30日 16:16

@刘承川 别装了。。等等就有了

李鑫4月1日 11:50

现在有了吗

长孙无限4月1日 14:23

并没有，可以在本地手搓，把sdk切换到cli

李翔4月8日 14:22

现在🦐有这个能力了嘛？

王冠梓4月9日 16:32

有了吗？

贾琳(瓦力)昨天 15:11

有了吗

贾琳(瓦力)昨天 15:12

给个时间点，有了就不自己折腾了

回复...

user6056453月31日 22:00

为什么openclaw是单独的呢，claude code和别的agent要从github配置

牛晶泾3月31日 22:03

后续 openclaw 会由官方直接完成对接。

user6056454月2日 07:25

@牛晶泾 嗯嗯，但想知道区别在哪，为啥openclaw跟别的agent是不一样的呢

牛晶泾4月2日 10:13

Openclaw 自身带了飞书操作能力，和 CLI 放在一起可能会有冲突。

Justin574月3日 13:08

@牛晶泾 有日程了吗？

user6056454月3日 13:19

@牛晶泾 噢噢明白了 谢谢！

回复...