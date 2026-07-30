---
title: Obsidian 四层架构
created: 2026-07-30
updated: 2026-07-30
sources:
  - "[[Clippings/articles/Obsidian 的 13 种内容形式.md]]"
tags: [Obsidian, 知识管理, 架构, 方法论]
status: draft
---

# Obsidian 四层架构

> Obsidian 不是"又一个 Markdown 编辑器"，而是一套从单篇笔记到知识网络的完整四层建筑体系。

---

## 四层模型

### 第一层：Markdown（建造每栋房子）

标准 Markdown 负责**单篇文章的组织**——层级、并列、顺序、引用、关联。

核心理念：**知识依赖结构而非样式**。一本书去掉颜色字体仍清晰，Markdown 保存的就是信息的结构关系。人类表达信息的关系本质只有几种，Markdown 将其符号化。

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L155-159

### 第二层：双向链接（修建道路）

`[[笔记名]]` 不是传统超链接，而是**建立笔记间的关联**，把孤立文章编织成网络。

关键区别：
- 标准 Markdown 链接是硬编码路径，文件移动/改名即断
- Obsidian 的 `[[笔记名]]` 是**全局索引**，内部重命名/移动时自动更新

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L108-113

### 第三层：Frontmatter（建立房屋档案）

YAML 元数据区分离了"正文说了什么"与"笔记是什么"，使每篇笔记成为**可管理的数据对象**。

核心应用：
- 配合 Dataview 按标签、状态、时间筛选全库笔记
- `aliases` 别名实现文件名不变但全局可索引

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L17-21

### 第四层：Dataview、Canvas、图谱（管理整座城市）

在笔记网络之上提供**查询、可视化、管理能力**：
- Dataview：SQL-like 查询全库元数据
- Canvas：可视化卡片布局，头脑风暴
- 图谱：关系可视化

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L162-163

---

## 核心思想

知识的价值取决于三个维度：
1. **结构是否清晰**（层级、并列、顺序）
2. **关系是否明确**（链接、引用、嵌入）
3. **数据是否可管理**（元数据、查询、可视化）

学会用"结构"思考笔记，才是长期积累的关键。

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L165-166

---

## 相关概念

- [[tools/Obsidian]]
- [[concepts/Zettelkasten]]
- [[concepts/MOC]]
- [[concepts/第二大脑]]

## 来源

- [[Clippings/articles/Obsidian 的 13 种内容形式.md]]
