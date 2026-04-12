---
title: "一定要用 Claude 管理你的 Obsidian，这才是真正的生产力"
source: "https://zhuanlan.zhihu.com/p/2010739583546040891"
author:
  - "[[東方幽静響]]"
published:
created: 2026-04-12
description: "说个现实的问题，现在搞 AI 编程的人越来越多，但大多数人的知识管理还停留在\"收藏夹吃灰\"的阶段。看到好文章收藏一下，遇到好工具截个图，然后就没有然后了。 我之前也是这样。直到最近装了一个叫 Claudi…"
tags:
  - "clippings"
---
说个现实的问题，现在搞 AI 编程的人越来越多，但大多数人的知识管理还停留在"收藏夹吃灰"的阶段。看到好文章收藏一下，遇到好工具截个图，然后就没有然后了。

我之前也是这样。直到最近装了一个叫 [Claudian](https://zhida.zhihu.com/search?content_id=270726292&content_type=Article&match_order=1&q=Claudian&zhida_source=entity) 的 [Obsidian](https://zhida.zhihu.com/search?content_id=270726292&content_type=Article&match_order=1&q=Obsidian&zhida_source=entity) 插件，直接把 [Claude Code](https://zhida.zhihu.com/search?content_id=270726292&content_type=Article&match_order=1&q=Claude+Code&zhida_source=entity) 嵌进了 Obsidian 里面——侧边栏打开就是 AI 聊天面板，你的整个笔记库自动变成 Claude 的工作目录。读写笔记、跨文档整理、自动建双向链接，全在 Obsidian 里完成，不用切终端。

今天把搭建过程和我的知识管理实操分享出来。

---

## 为什么是 Claude + Obsidian

先说说为什么选这个组合。

**Obsidian** 不用多介绍了，本地 Markdown 笔记工具，数据全在自己手里，插件生态丰富。关键是 Markdown 格式对 AI 极其友好——纯文本、结构化、没有乱七八糟的富文本格式，AI 读起来毫无障碍。

**Claude Code** 是 Anthropic 出的 AI 编程 Agent，能力很强。但直接用有两个痛点：一是只能用自家模型，官方 API 价格不便宜；二是国内网络访问有门槛。不过这两个问题都有解法，后面会讲。

关键在于 **Claudian** 这个插件——它把 Claude Code 的全部能力直接嵌入到了 Obsidian 内部。装完之后，Obsidian 侧边栏就多了一个 AI 聊天面板，你的笔记库自动成为 Claude 的工作目录。

这意味着什么？

- 在 Obsidian 里直接跟 Claude 对话，AI 可以读写你的所有笔记
- 想整理某个技术主题，一句话让 AI 跨文档做关联、打标签、生成摘要
- 选中一段文字按快捷键，Claude 直接帮你改写，带 diff 预览
- 素材丢进去不用管格式，后面让 AI 帮你结构化整理
- 用 `@` 提及文件，Claude 自动读取上下文

说白了，你的 Obsidian 笔记库不再只是一个"存东西的地方"，而是变成了一个 AI 可以操作的知识引擎。

---

## 第一步：用 cc-switch 解决模型配置问题

在装 Claudian 之前，先把模型环境配好。

Claudian 底层依赖 Claude Code CLI，而 Claude Code 默认绑定 Anthropic 官方 API，价格贵不说，国内网络访问也是个问题。如果想切换到第三方中转 API 或者国产模型，需要手动改配置文件，非常麻烦。

**cc-switch** 就是解决这个问题的工具，一个开源的配置管理桌面应用（项目地址： [github.com/farion1231/c](https://link.zhihu.com/?target=https%3A//github.com/farion1231/cc-switch) ）。

它能做三件事：

1. **一键切换模型/API 供应商** ：点一下就能把底层模型从官方 API 切到便宜的第三方中转，或者国产兼容模型（DeepSeek、Kimi、GLM、 [MiniMax](https://zhida.zhihu.com/search?content_id=270726292&content_type=Article&match_order=1&q=MiniMax&zhida_source=entity) 等）
2. **MCP** **与 Skills 管理** ：可视化界面，一键安装和管理 MCP 服务器和各种插件技能
3. **提示词管理与测速** ：内置测速功能，还能管理多套系统提示词

安装很简单，下载打开就能用：

![](https://picx.zhimg.com/v2-a7c1d96c8d4a46b3f94226b9fb5c4af3_1440w.jpg)

比如我这里加了 MiniMax 的 API，配置好之后一键切换：

![](https://picx.zhimg.com/v2-9487ac0ab6b63cc91b25b31240532c27_1440w.jpg)

配置完 cc-switch 后，Claudian 底层就会用你配置好的模型，不用登录 Anthropic 官方账号：

![](https://pic4.zhimg.com/v2-6bbb7ad34df9763fff7524aa1af5778f_1440w.jpg)

这一步搞定之后，后面在 Obsidian 里用 Claude 就可以走便宜的中转 API 了，成本低很多。

---

## 第二步：安装 Claudian，把 Claude 嵌入 Obsidian

环境配好了，接下来装关键插件—— **Claudian** 。

先说个背景。Obsidian 官方最近发布了 CLI（命令行接口），这是一个值得关注的趋势：越来越多的传统工具开始为 AI Agent 开发接口。

![](https://pic4.zhimg.com/v2-e4fb4bfcc53d318e7e0e171a5964540b_1440w.jpg)

Claudian 就是基于这个能力做的 Obsidian 插件，2.8k star，它做的事情很直接： **把 Claude Code 的完整能力嵌入到 Obsidian 的侧边栏里** 。

装完之后你会得到：

- **侧边栏聊天面板** ：点机器人图标或命令面板打开，直接在 Obsidian 里跟 Claude 对话
- **内联编辑** ：选中文字 + 快捷键，Claude 直接改写，带 word-level diff 预览
- **上下文感知** ：自动附带当前打开的笔记，用 `@` 提及其他文件
- **Skills 支持** ：可以加载各种技能包，扩展 Claude 的能力
- **MCP 支持** ：接入外部工具和数据源
- **图片识别** ：拖拽或粘贴图片，Claude 直接分析

不得不说，以前你要让 AI 操作 Obsidian，得在终端里跑 Claude Code 然后指向笔记库目录。现在有了 Claudian，全在 Obsidian 里完成，体验好太多了。

### 安装方式：直接让 AI 装

现在安装插件都不用手动下载了。

我在 Claude Code 里输了一句话： **"帮我为这个文件所在的 Obsidian 库安装 claudian 插件并打开"** ，AI 就自动完成了整个安装流程——下载插件、放到正确目录、启用插件，一气呵成。

![](https://pic2.zhimg.com/v2-ced1a1aa858e8452107e7dfdb5d43b61_1440w.jpg)

![](https://pic1.zhimg.com/v2-c49383112dfdca24850db2c3ea1957e4_1440w.jpg)

说个有意思的事，我这次底层用的模型是国产的 MiniMax（通过 cc-switch 切换的），安装过程一点问题没有。国产模型应对这类工具操作任务已经完全没问题了，进步确实很大。

安装完成后，在 Obsidian 里就能看到 Claudian 的聊天面板了：

![](https://pic4.zhimg.com/v2-38ed8084ae8d89761e6d250d0d4d8db9_1440w.jpg)

---

## 第三步：安装 Obsidian Skills，教会 Claude 理解你的笔记

光装 Claudian 还不够，还要装 **Obsidian Skills** （项目地址： [github.com/kepano/obsid](https://link.zhihu.com/?target=https%3A//github.com/kepano/obsidian-skills) ）。

Skills 是什么？说白了就是一套"技能说明书"，告诉 Claude 怎么正确操作 Obsidian。没有 Skills，Claude 写出来的 Markdown 可能不符合 Obsidian 的语法规范；有了 Skills，它就知道怎么用 wikilinks、callouts、properties 这些 Obsidian 特有的语法。

目前官方提供了 5 个 Skill：

| Skill | 作用 |
| --- | --- |
| obsidian-markdown | 教 AI 写 Obsidian 风格的 Markdown（wikilinks、embeds、callouts、properties 等） |
| obsidian-bases | 操作 Obsidian Bases（视图、过滤器、公式、汇总） |
| json-canvas | 创建和编辑 JSON Canvas 画布文件 |
| obsidian-cli | 通过 CLI 操作 Obsidian（插件管理、主题开发等） |
| defuddle | 从网页提取干净的 Markdown，去掉杂质省 token |

其中 **obsidian-markdown** 和 **obsidian-cli** 是最常用的，建议必装。 **defuddle** 也很实用，比如你想把一篇网页文章存到笔记库里，它能帮你提取干净的内容，不会带一堆广告和导航栏。

安装方式同样可以让 AI 帮你搞定，或者手动把 skills 目录放到笔记库的 `.claude/skills/` 下面就行。

---

## 搭好之后能干什么：我的知识管理实操

工具搭好了，说说我实际怎么用的。

**素材收集：丢进去就行**

看到好文章、好观点、有价值的讨论，直接存到 Obsidian 的素材目录里。不用整理格式，不用打标签，原始内容丢进去就行。以前我总想着"等有空了再整理"，结果永远没空。现在不用了，后面 AI 会帮你处理。

**知识整理：在 Obsidian 里一句话搞定**

打开 Claudian 的聊天面板，直接说"把 materials 目录下所有关于 AI 编程工具的素材整理成一个主题笔记，按工具分类，每个工具列出核心功能、价格、适合场景"。

Claude 会自动读取相关文件、提取关键信息、生成结构化的笔记，直接写到你指定的位置。这个效率比手动整理快了不知道多少倍。

**跨文档关联：AI 帮你连点成线**

Obsidian 最强的能力之一是双向链接，但手动建链接太累了。现在可以让 AI 帮你做——"检查这篇笔记，找出和库里其他笔记的关联，帮我加上双向链接"。Claude 会扫描你的笔记库，找到语义相关的内容，自动建立链接。

**内联编辑：选中就改**

写笔记的时候觉得某段话不够好？选中那段文字，按快捷键，Claude 直接帮你改写，还带 diff 预览，改了哪里一目了然。

这才是知识管理该有的样子：你只管往里丢东西，AI 帮你整理、关联、结构化。

---

## 写在最后

说白了，这套组合的核心思路就一句话： **让你的知识库对 AI 可编程** 。

Obsidian 提供了本地化、结构化的数据基础，Claudian 把 Claude 的 AI Agent 能力直接嵌入 Obsidian 内部，Obsidian Skills 教会 Claude 正确操作你的笔记，cc-switch 解决了国内使用的成本和网络问题。

四个东西加在一起，你的笔记库就从一个静态的文件夹，变成了一个 AI 可以操作的知识引擎。

未来的个人知识库竞争，拼的不是谁存的东西多，而是谁的知识库对 AI 更友好。现在花点时间把这套东西搭起来，后面会越用越顺。

来源： [mp.weixin.qq.com/s/AJv\_](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/AJv_hBTmoXVH0WVO7veoBw)

编辑于 2026-02-27 15:35・湖南