---
title: "llm Wiki 养了三周，开始出毛病了"
source: "https://mp.weixin.qq.com/s/Zoqc9uizk6NsGgAW3ItOTw"
author:
  - "[[AI赋能说]]"
published:
created: 2026-04-30
description: "上次说，转发即沉淀。飞轮转起来了。转了三周。wiki/ 目录下多了六十几个页面。index.md 越来越长。"
tags:
  - "clippings"
---
AI赋能说 *2026年4月22日 18:56*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/B9Tu6L8wd2YhCCZGAMglKTkEM5a6cKyWFm1lE7btDBSdQ2ibeXENUs5ryshVIjk6HzdCs3R5Is1BwLqdPrXUwJkBhObic7Rk6L2TsjIBN8Uu4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

上次说， [转发即沉淀](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg==&mid=2247488416&idx=1&sn=75307472a5300ceb231d6464b9d8721d&scene=21#wechat_redirect) 。飞轮转起来了。

转了三周。

wiki/ 目录下多了六十几个页面。index.md 越来越长。log.md 记了上百条操作。

看起来一切正常。

直到有一天，我问了一个问题。AI 给了一个很自信的回答。引用了三个 wiki 页面。

我顺手点进去看了一眼。

其中一个页面里的数字，和原始文章里的不一样。

原文写的是 47.2%。wiki 页面写的是"接近一半"。

不算错。但也不算对。

又翻了几个页面。发现类似的情况不止一处。有的是数字被四舍五入了。有的是一个有前提条件的结论，前提被省略了。有的是两篇文章说了不同的事，wiki 页面只保留了其中一个。

每一处偏差都很小。但它们在互相引用。A 页面引用了 B 页面的结论，B 页面引用了 C 页面的数据。链条越长，偏差越大。

而 AI 每次回答都很自信。因为 wiki 页面之间是一致的。

只是和原始文档不一致了。

这就是知识漂移。

Karpathy 的 Gist 评论区里，有人分享了一模一样的经历。他们让 AI 生成摘要，把摘要当知识源。健康检查每次都通过——因为检查只验证摘要之间是否一致，不验证摘要是否还忠于原文。几个月后才发现，系统已经"自信地犯错"了很久。

想了想。这个问题不是 bug。是所有"AI 写的东西当作知识"的系统都会遇到的结构性问题。

AI 生成的摘要是有损压缩。每次更新都可能引入微小偏差。偏差不会自己消失。只会在互相引用中放大。

## 三个毛病，三个解法

用了三周，我遇到了三个毛病。知识漂移只是其中一个。

**毛病一：漂移。** Wiki 页面和原始文档慢慢脱节。上面说了。

**毛病二：孤岛。** 有些页面写完就没人引用了。它们存在，但不在任何知识链条里。等于死了。

**毛病三：找不到。** Wiki 超过五十页之后，AI 开始"忘记"早期的内容。不是真的忘了，是 index.md 太长，AI 在里面找东西的效率变低了。

三个毛病，对应三个解法。

## 解法一：给 Wiki 加溯源

漂移的根源是什么？是 wiki 页面里的事实，和原始文档之间断了链。

解法很简单。每个关键事实后面，标注来源的具体位置。

不是标注"来自 raw/xxx.md"。是标注"来自 raw/xxx.md 第 42-45 行"。

```
该公司营收"10.3 亿元"。
— raw/annual-report.md, L128
```

这样做有两个好处。

第一，你自己检查的时候，一秒钟就能跳到原文验证。

第二，AI 做健康检查的时候，可以自动对比 wiki 页面里的事实和原文是否一致。不是检查 wiki 页面之间的一致性——那个没用。是检查 wiki 页面和 raw/ 之间的一致性。

在 AGENTS.md 里加一条规则：

```
数字、百分比、具体结论，必须原文引用并标注来源行号。
不要用 AI 的话重述数字。
```

这条规则很小。但它是防漂移的第一道防线。

## 解法二：定期体检

Karpathy 原文里提到了 Lint 操作。但只说了"定期让 AI 检查 wiki 健康状况"，没有说具体检查什么。

用了三周之后，我觉得体检至少要查五件事。

**矛盾。** 同一个事实在不同页面上说法不同。

**过时。** raw/ 里的素材更新了，但对应的 wiki 页面没更新。

**孤岛。** 没有任何其他页面链接到的页面。

**断链。** 引用了一个不存在的页面。

**漂移。** 随机抽几个摘要页面，逐条对比原始文档。

前四个是常规体检。第五个是深度体检。

常规体检每周做一次。对 AI 说"体检"就行。

深度体检每月做一次。对 AI 说：

```
深度体检：随机抽 5 个摘要页面，逐条对比原始文档
```

AI 会读摘要，读原文，逐条比对，报告偏差，然后修复。

这是防漂移的最后一道防线。

## 解法三：给 Wiki 加搜索

index.md 是 Karpathy 设计里的导航核心。AI 每次回答问题，先读 index.md，找到相关页面，再深入读取。

这在 wiki 小的时候很好用。但超过五十页之后，index.md 本身就占了很多 token。AI 在里面"找东西"的效率开始下降。

Gist 评论区里有人做了一个实验。1602 个素材，生成了 161 个 wiki 页面。到 150 页左右的时候，他发现自己已经不看 index.md 了——改用 Obsidian 的图谱视图导航。

图谱视图的好处是直觉。哪些页面是枢纽（被大量引用），哪些是孤岛（没有链接），一眼就看到。

但 AI 看不到图谱视图。它需要一个搜索工具。

Karpathy 推荐了 qmd <sup>[1]</sup> 。本地 Markdown 搜索引擎，BM25 + 向量混合搜索，全部在本地跑。有 CLI 和 MCP Server 两种模式。MCP 模式下 AI Agent 可以直接调用。

如果不想装额外工具，一个简单的 grep 脚本也够用：

```
grep -ril "$1" ~/my-wiki/wiki/ | head -20
```

关键不是用什么工具。关键是：当 wiki 大到 index.md 装不下的时候，你需要一个 AI 能调用的搜索入口。否则 AI 会开始"忘记"早期的知识。不是真的忘了。是找不到了。

## 评论区里最精彩的一段话

Gist 评论区吵得很凶。有人说 LLM Wiki 是天才设计，有人说它根本不能用。

但最精彩的一段话，来自一个叫 @gulliveruk 的开发者。他说：

> ❝
> 
> 确定范围应该是确定性的，推理应该是概率性的。

什么意思？

当你问"哪些页面和这个问题相关"，这个"找范围"的操作应该是精确的。用标签过滤、用元数据查询、用搜索引擎检索。不应该让 AI 去"猜"。

AI 应该做的是：在已经精确筛选出的小范围内，做推理和综合。

把"找"和"想"分开。找的部分交给确定性工具。想的部分交给 AI。

这可能是 LLM Wiki 下一步进化的方向。wiki 页面依然是人类可读的知识层。但在它旁边，需要一层确定性的检索结构——标签、元数据、搜索索引，甚至知识图谱。

AI 不再从 index.md 里"猜"哪些页面相关。而是从检索层里"查"到相关页面，然后只在这些页面上做推理。

## 还有一件事

Gist 发出三周。5000+ star。近 5000 fork。

但 Karpathy 自己没有发布任何产品。没有代码。没有工具。只有一个 idea file。

社区长出了几十个实现。有人做了 Obsidian 插件。有人做了 macOS 桌面应用。有人做了 Claude Code Skill。有人把它接到了微信。有人把它用在了客户管理。有人把它用在了军事条令。

一个想法，没有代码，5000 star。

想了想。这本身就是 LLM Wiki 思路的一个证明。

Karpathy 没有写代码。他写了一份 Schema。一份告诉别人"这个系统应该怎么组织"的规则文档。

然后让整个社区当他的 Agent，去执行这份 Schema。

和 LLM Wiki 里 AI 的角色一模一样。

人定规则。Agent 执行。知识复利。

只不过这次，Agent 是几千个开发者。

## 想了想

第二篇说， [转发即沉淀](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg==&mid=2247488416&idx=1&sn=75307472a5300ceb231d6464b9d8721d&scene=21#wechat_redirect) 。

这一篇想说的是： **养 Wiki 和养花一样。不是种下去就完了。得浇水，得除草，得定期检查根有没有烂。**

AI 是园丁。它可以浇水、除草、修枝。

但种什么花，开什么园，哪棵该留哪棵该剪——还是你说了算。

Karpathy 在 Gist 里写了一句很清醒的话：Human owns verification。

LLM 可以维护 wiki。但最终验证的责任还是在人。

三周前我搭了一个 wiki。三周后我学会了怎么养它。

下一步，大概是学会怎么让它长得更大而不失控。

但那是下一篇的事了。

参考资料：Karpathy llm-wiki.md gist <sup>[2]</sup> · Gist 评论区讨论 <sup>[3]</sup> · 从 Karpathy 的第二大脑到 Entropy <sup>[4]</sup> · OpenWiki 桌面实现 <sup>[5]</sup> · qmd 本地搜索引擎 <sup>[6]</sup> · RAG 还是学习？连续知识漂移下的 LLM 适应极限 <sup>[7]</sup>

Reference

\[1\]

qmd: *https://github.com/tobi/qmd*

\[2\]

Karpathy llm-wiki.md gist: *https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f*

\[3\]

Gist 评论区讨论: *https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink\_comment\_id=6109752#gistcomment-6109752*

\[4\]

从 Karpathy 的第二大脑到 Entropy: *https://trilogyai.substack.com/p/from-karpathys-second-brain-to-entropy*

\[5\]

OpenWiki 桌面实现: *https://github.com/kdsz001/OpenWiki*

\[6\]

qmd 本地搜索引擎: *https://github.com/tobi/qmd*

\[7\]

RAG 还是学习？连续知识漂移下的 LLM 适应极限: *https://arxiv.org/html/2604.05096v1*

**下方是赋能君的AI学习交流永久免费星球，想学习更多内容，欢迎扫码加入。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

🙌 如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是同道中人，所以如果你有自认为不错的信息获取渠道，欢迎留言或者私聊我，谢谢。

都看到这里了，就给个关注吧👀：

喜欢我的文章，可以请你右下角顺手来一波点赞&在看&分享三连么👉

AI工具 · 目录

继续滑动看下一个

AI赋能说

向上滑动看下一个