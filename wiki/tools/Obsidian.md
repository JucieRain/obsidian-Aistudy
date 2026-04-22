---
title: Obsidian
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
tags: [工具, 知识管理, 笔记, Markdown]
status: stable
---

# Obsidian

> 基于 Markdown 的知识管理工具，支持双向链接、图谱视图、插件扩展

## 核心特性

- **本地优先**：所有数据存储在本地，完全可控
- **双向链接**：`[[页面名]]` 创建可点击的内部链接
- **图谱视图**：可视化展示笔记之间的关联关系
- **插件生态**：丰富的社区插件扩展功能
- **Git 同步**：可通过 Git 实现跨设备同步

## 在 LLM Wiki 中的角色

Obsidian 是 Karpathy 方法的「IDE」：
- **Vault**：知识库的物理存储位置
- **wiki/ 目录**：AI 维护的结构化知识
- **图谱视图**：检查知识连接情况
- **Web Clipper**：剪藏网页素材到 Clippings/

## 关键插件

| 插件 | 功能 |
|-----|------|
| Web Clipper | 浏览器剪藏网页到 Markdown |
| Dataview | 查询 frontmatter 生成动态表格 |
| Obsidian Git | 自动 Git 同步 |
| Marp | Markdown 转 PPT |

## 配置建议

### Web Clipper 配置

- 默认剪藏目录：`Clippings/`
- 可自定义模板和 frontmatter

### 文件与链接设置

- 附件文件夹：`Clippings/assets/`
- 使用相对路径链接
- 绑定快捷键下载图片到本地

## 参见

- [[tools/Claude Code]]
- [[concepts/第二大脑]]
- [[concepts/LLM Wiki]]

## 来源

- [[Clippings/articles/Obsidian + Claude Code 教程.md]]