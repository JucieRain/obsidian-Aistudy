---
title: Obsidian Skills
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/一定要用 Claude 管理 Obsidian.md]]"
tags: [工具, Skills, Obsidian]
status: stable
---

# Obsidian Skills

> 教 Claude 正确操作 Obsidian 的技能包

## 核心作用

没有 Skills，Claude 可能写出不符合 Obsidian 语法的 Markdown。
有了 Skills，它知道 wikilinks、callouts、properties 等 Obsidian 特有语法。

## 官方 Skills

| Skill | 作用 |
|-----|------|
| **obsidian-markdown** | Obsidian 风格 Markdown（wikilinks、embeds、callouts） |
| **obsidian-bases** | 操作 Obsidian Bases（视图、过滤器、公式） |
| **json-canvas** | 创建 JSON Canvas 画布文件 |
| **obsidian-cli** | CLI 操作 Obsidian（插件管理、主题开发） |
| **defuddle** | 网页提取干净 Markdown，去掉杂质 |

## 必装推荐

- `obsidian-markdown`：必装
- `obsidian-cli`：必装
- `defuddle`：实用

## 安装方式

1. 让 AI 安装：「安装 obsidian-skills」
2. 手动：把 skills 目录放到 `.claude/skills/`

## 项目地址

GitHub：https://github.com/kepano/obsidian-skills

## 参见

- [[tools/Obsidian]]
- [[tools/Claudian]]

## 来源

- [[Clippings/articles/一定要用 Claude 管理 Obsidian.md]]