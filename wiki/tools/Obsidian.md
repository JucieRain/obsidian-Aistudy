---
title: Obsidian
created: 2026-04-22
updated: 2026-04-30
sources:
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
  - "[[Clippings/articles/磨砺你的思维。.md]]"
  - "[[Clippings/articles/Obsidian x Agent 终极指南，从零打造个人 Agent 系统]]"
  - "[[Clippings/articles/Obsidian Cli 基础使用教程 AI化知识管理全过程]]"
tags: [工具, 知识管理, 笔记, Markdown, AI操作系统]
status: stable
---

# Obsidian

> 免费且灵活的私人笔记应用，基于 Markdown 的知识管理工具，AI时代被重新审视为"AI的操作系统"

## 官方资源

| 资源 | 链接 |
|-----|------|
| **官网** | https://obsidian.md/zh |
| **下载** | https://obsidian.md/zh/download |
| **帮助文档** | https://obsidian.md/zh/help |
| **开发者文档** | https://docs.obsidian.md/ |

## 核心特性

### 本地优先

所有数据存储在本地 Markdown 文件：
- **完全可控**：数据永远属于你
- **跨平台**：Windows、macOS、Linux、iOS、Android
- **无锁定**：纯文本格式，随时可迁移

### 双向链接

`[[页面名]]` 创建可点击的内部链接：
- **链接一切**：想法、人物、地点、书籍等
- **个人维基百科**：构建自己的知识网络
- **反向链接**：自动显示哪些页面链接到当前页面

### 图谱视图

可视化展示笔记之间的关联关系：
- **发现隐藏模式**：直观的交互式图谱
- **知识结构检查**：一眼看清知识连接情况

### 白板 Canvas

无限的空间用于研究和头脑风暴：
- **绘制图表**：可视化思维流程
- **组织想法**：思维的无限游乐场
- 查看更多：https://obsidian.md/zh/canvas

### 插件生态

打造理想的思考空间：
- **数千个插件**：社区贡献的功能扩展
- **开放 API**：创建自己的插件和主题
- 查看更多：https://obsidian.md/zh/plugins

## 官方服务

### Obsidian Sync

安全同步，端到端加密保护：
- **版本历史**：每条笔记保留一年的版本历史
- **协作**：与团队共享文件协作
- **精细控制**：选择同步哪些文件和设备
- 查看更多：https://obsidian.md/zh/sync

### Obsidian Publish

即时发布为在线知识库：
- **无缝编辑**：从应用即时发布笔记
- **自定义**：主题、域名、密码保护
- **SEO 优化**：速度快、移动端友好
- 查看更多：https://obsidian.md/zh/publish

## AI时代的新视角：AI的工作桌

Obsidian 是 AI 的操作系统，是 Claude Code 的工作台、是个人上下文的资料库、是 Agent 能伸手就拿到所有材料的那张桌子。

### 类比：请助理的准备

你请了一个助理，想让他帮你处理工作：
- 给他一张桌子（有权限能随时拿到所有材料）
- 桌上按分类摆好文件夹（客户资料、项目档案、个人偏好）
- 贴几张便利贴（写清楚哪些规则不能违反）
- 桌角放一本 SOP（不同任务按什么流程做）
- 给他一支笔，让他能随手记、随手写

Obsidian 就是这张桌子的数字版，Agent 就是那个助理。

### Karpathy 三件套

| 套件 | 内容 | 作用 |
|-----|------|------|
| **剪藏** | 所有入口都是 Obsidian | 不在 Obsidian 里的信息对 AI 系统等于不存在 |
| **Wiki** | `[[概念名]]` 让信息自己组织 | AI 读到任何笔记都能顺着双链拿到背景 |
| **规则** | CLAUDE.md 告诉 AI 怎么工作 | 哪些该做、不该做、不同任务怎么走 |

## CLI 能力（v1.12+）

Obsidian v1.12 正式发布命令行接口（CLI），能通过命令行实现所有操作。

### URI Scheme

通过 `obsidian://` 协议直接操作：

| 操作 | URI |
|-----|-----|
| 新建文件 | `obsidian://new?vault=Vault名&name=文件名&content=内容` |
| 打开文件 | `obsidian://open?vault=Vault名&file=路径/文件名` |
| 搜索 | `obsidian://search?vault=Vault名&query=关键词` |

### 配合 Claude Code

AI 能直接 `cat`、`grep`、`rg` 遍历整个 Vault，按需加载上下文。

本地文件加本地 CLI，是目前 AI 读写个人知识最低成本的方案。

详见 [[practices/Obsidian CLI配置指南]]

## 在 LLM Wiki 中的角色

Obsidian 是 Karpathy 方法的「IDE」：
- **Vault**：知识库的物理存储位置
- **wiki/ 目录**：AI 维护的结构化知识
- **图谱视图**：检查知识连接情况
- **Web Clipper**：剪藏网页素材到 Clippings/
- **CLI**：让 AI 直接进入仓库操作

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
- [[tools/Claudian]] - Claude Code 嵌入 Obsidian 的插件
- [[tools/Web Clipper]] - 网页剪藏
- [[concepts/第二大脑]]
- [[concepts/LLM Wiki]]
- [[people/空格丶]] - AI操作系统视角提出者
- [[people/ShikiLab]] - CLI配置教程作者
- [[practices/Obsidian CLI配置指南]]

## 来源

- [[Clippings/articles/Obsidian + Claude Code 教程.md]]
- [[Clippings/articles/Obsidian x Agent 终极指南，从零打造个人 Agent 系统]]
- [[Clippings/articles/Obsidian Cli 基础使用教程 AI化知识管理全过程]]