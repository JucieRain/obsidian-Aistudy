---
title: "用Karpathy 的 LLM Wiki 方法, 我把 Obsidian 改造成了一个会成长的知识系统"
source: "https://zhuanlan.zhihu.com/p/2025975555867059197"
author:
  - "[[蝈蝈的AI笔记公众号: 蝈蝈的AI笔记]]"
  - "[[专注:AI智能体/AI工具提效]]"
published:
created: 2026-04-11
description: "哈喽，大家好，我是蝈蝈。 我平时在网上会看到很多很好的文章，也一直在收藏。但收藏久了就发现，它们大多只是躺在收藏夹里吃灰。没有一个统一的地方去收集、整理和回看，后面更谈不上把它们真正消化成自己的东西…"
tags:
  - "clippings"
---
哈喽，大家好，我是蝈蝈。

我平时在网上会看到很多很好的文章，也一直在收藏。但收藏久了就发现，它们大多只是躺在收藏夹里吃灰。没有一个统一的地方去收集、整理和回看，后面更谈不上把它们真正消化成自己的东西。

最近看到 [Karpathy](https://zhida.zhihu.com/search?content_id=272872013&content_type=Article&match_order=1&q=Karpathy&zhida_source=entity) 写的这篇基于大模型来改造个人知识库 [LLM Wiki](https://zhida.zhihu.com/search?content_id=272872013&content_type=Article&match_order=1&q=LLM+Wiki&zhida_source=entity) 文章，很受启发。

[gist.github.com/karpath](https://link.zhihu.com/?target=https%3A//gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

![](https://pic3.zhimg.com/v2-79d9bed2c1d7c185c8489ae5cfcbc240_1440w.jpg)

Karpathy的核心思路就是，把知识管理从临时检索，变成持续编译。

传统 RAG 的习惯是每次提问都去原文里现找现拼，答案能出来，但不会沉淀。

LLM Wiki 的思路不一样，它在原文和问答之间放了一层持久化 wiki。每次新增资料，LLM 都会把关键信息写进已有结构，更新主题页、实体页、总结页，还会标注新旧观点的冲突和变化。

它不是一次性的问答系统，更像一个会自己长大的知识系统。

### LLM Wiki 的底层框架

LLM Wiki 的底层结构和操作流程，其实并不复杂。

### 三层架构

- `Raw sources：` 原始资料层，尽量不可改，是事实来源
- `Wiki：` 结构化知识层，LLM 负责写和维护
- `Schema：` 规则层，定义目录、命名、工作流和质量标准

### 三个核心操作

- `Ingest：` 摄入新资料并更新多页
- `Query：` 基于 wiki 回答问题，答案可回写为新页面
- `Lint：` 定期体检，查冲突、过期、孤儿页、缺链接、缺主题

### 把这套思路落地到 Obsidian

说干就干，我让 [Codex](https://zhida.zhihu.com/search?content_id=272872013&content_type=Article&match_order=1&q=Codex&zhida_source=entity) 全程协作，负责执行和校验，我负责目标和取舍判断。

最后落到我自己的库里，是一个四层骨架，规则层 schema、原文层 raw、知识层 wiki，再加一个操作层 ops。

- `00_schema` 放规则和迁移报告
- `01_raw` 只放原文真源
- `02_wiki` 放结构化知识页面
- `03_ops` 放脚本、模板和自动化
![](https://pic2.zhimg.com/v2-575f9a91527b4fe7d2c9afdf8df2cd07_1440w.jpg)

原先 Obsidian 里的历史文章，我没有改正文，一个字都没动，全部迁到 `01_raw。`

### 关键一步是让它自动跑起来

后面最关键的一步，是在 ops 层补增量同步脚本。

它每 30 分钟跑一次，扫描 raw 里的新稿，补齐到 wiki 层，再把实体、概念、主题、综述、巡检串起来跑完, 当然这些wiki层都是AI来维护, 我们不用太关心。

你不用每次手工点一堆地方，系统会自己执行。

![](https://pica.zhimg.com/v2-81eb3efd5e3688ddd5a8fe9fd93fa630_1440w.jpg)

### 我现在每天怎么用

我现在每天的动作其实很简单。

用 Karpathy文章里提到的浏览器插件 [Obsidian Web Clipper](https://zhida.zhihu.com/search?content_id=272872013&content_type=Article&match_order=1&q=Obsidian+Web+Clipper&zhida_source=entity) 收集一篇文章，直接丢进 raw 层。

![](https://pic2.zhimg.com/v2-6533df47347a42dcec8eb80984071995_1440w.jpg)

后面脚本会定时自己跑，把新素材编译进 wiki 的索引和关联。

我再去 wiki 层看 `topic` 和 `synthesis` 页面，直接开始写作和思考。

### 改造后的目录主干

| 目录/文件 | 作用 | 谁来维护 |
| --- | --- | --- |
| 00\_schema/ | 规则层，放知识库运行规则和迁移文档 | 人 + AI |
| 00\_schema/AGENTS.md | 全局工作规范，定义目录约定、流程、注意事项 | 人 + AI |
| 01\_raw/ | 原始资料层，放你收集的原文和笔记 | 人 |
| 02\_wiki/ | LLM 编译后的知识层，真正用于检索、问答、写作复用 | AI |
| 02\_wiki/sources/ | 每篇原始资料对应的“source 页面” | AI |
| 02\_wiki/topics/ | 主题页，按主题聚合 sources 的内容 | AI |
| 02\_wiki/synthesis/ | 主题综述页，跨多篇资料的综合结论 | AI |
| 03\_ops/ | 运维层，放自动化、脚本、配置、日志 | AI |
| 03\_ops/scripts/ | 同步、构建、lint、归档等脚本 | AI |
| 03\_ops/automation/ | 定时任务配置（30分钟跑一次等） | AI |

一句话总结:

`00_schema` 负责规则和追溯， `01_raw` 负责原始资料， `02_wiki` 负责知识编译， `03_ops` 负责自动化运行。

### 实测体验

比如我上面刚收录了一篇 [Claude Code](https://zhida.zhihu.com/search?content_id=272872013&content_type=Article&match_order=1&q=Claude+Code&zhida_source=entity) 架构相关的文章，我就直接问 Claude Code 架构的问题。

![](https://pic1.zhimg.com/v2-212ec547164a6c2ce5f51dc3f45919e6_1440w.jpg)

它会检索到我 Obsidian 知识库里具体的文章来源。

![](https://pic1.zhimg.com/v2-5afe52265b87ee80b5a17a7285bd9098_1440w.jpg)

它的回答也不是单篇复述，而是基于知识库里的多篇资料做交叉归纳。

我自己用下来，最明显的变化有三点。

- 检索更快了，也更准了
- 写作更顺了，过去沉淀过的知识点更容易被调出来复用
- 问答过程中产出的好结论可以回写到知识库，后面还能继续迭代

### 快速改造

这套东西也不是银弹。要运行得好需要伴随持续性地维护。

如果你丢进去的原文本身就很散，或者长期不做巡检，系统会越来越大，但不一定越来越准。

它是一个持续维护的工作台，不是一次性搭完就完事的工程。

如果你今天就想开始，给你一个最快的改造方式:

用你本地的claude code / codex / openclaw, 把这篇文章或者Karpathy那篇文章直接丢给AI, 让它参考对本地的obsidian目录进行改造即可.

操作时尽量保留原来知识库的结构, 可以分批次先把最近最常看到的目录迁移到到 raw 层, 把流程跑通后再把剩下批次的原文来做迁移.

### 结语

现在再看自己的知识库，终于像个活系统了, 一个可以持续生长、持续复用、持续修正的工作台。

AI 时代每个人都该训练自己的个人知识库外脑。

不论你是产品、开发、运营，或者只是一个认真学习的人，这套个人知识库思路都能用。 因为我们真正要解决的问题，从来不是记更多笔记，而是能不能在关键时刻，把过去的知识积累调出来，连起来，用起来。

---

以上，既然看到这里了，如果觉得有帮助，欢迎点个赞、在看、转发三连。

欢迎留言说说，你的个人知识库构建的心得。

还没有人送礼物，鼓励一下作者吧

编辑于 2026-04-10 16:39・天津[Karpathy](https://www.zhihu.com/topic/29050338)[LLM](https://www.zhihu.com/topic/20660508)[个人wiki](https://www.zhihu.com/topic/19780556)