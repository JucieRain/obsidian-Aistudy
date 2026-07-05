---
title: PARA
created: 2026-07-05
updated: 2026-07-05
sources: ["[[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]"]
tags: [概念, 知识管理, 方法论, 组织]
status: stable
---

# PARA

> Tiago Forte 提出的个人知识组织框架：按可操作性将信息分为四层

## 核心结构

| 层级 | 含义 | 说明 |
|------|------|------|
| **P**rojects | 活跃项目 | 有明确截止日期和交付物的短期任务 |
| **A**reas | 持续领域 | 无截止日期、需要长期维护的责任领域 |
| **R**esources | 参考资料 | 未来可能用到的主题或兴趣 |
| **A**rchives | 归档 | 已完成或不活跃的项目/资料 |

## 核心原则

- 回答的问题：「这条信息放在哪里？」
- 越靠上越活跃，越靠下越静止
- 信息自然从 P → A → R → A 流动

## 在 Obsidian 中的应用

```
MyBrain/
├── 00-Inbox/          # 所有新内容入口
├── 01-Projects/       # 活跃项目
├── 02-Areas/          # 持续关注的领域
├── 03-Resources/      # 参考资料
├── 04-Archives/       # 已完成/不活跃
├── 05-Templates/      # 模板
├── 06-Attachments/    # 图片、PDF
└── 07-Daily/          # 每日笔记
```

> 原则：文件夹只是粗分区，真正的组织靠 [[双向链接]] 和 MOC。

> — [[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]], L60-80

## 与其他方法的关系

PARA 常与 Zettelkasten、MOC 融合使用：
- PARA 作行动枢纽（文件夹层面）
- Zettelkasten 作洞察引擎（链接原子笔记）
- MOC 作导航层（主题索引）

## 参见

- [[concepts/Zettelkasten]]
- [[concepts/MOC]]
- [[tools/Obsidian]]
