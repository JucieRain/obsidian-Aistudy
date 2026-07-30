---
title: Obsidian
created: 2026-04-22
updated: 2026-07-30
sources:
  - "[[Clippings/articles/Obsidian + Claude Code 教程.md]]"
  - "[[Clippings/articles/磨砺你的思维。.md]]"
  - "[[Clippings/articles/Obsidian x Agent 终极指南，从零打造个人 Agent 系统]]"
  - "[[Clippings/articles/Obsidian Cli 基础使用教程 AI化知识管理全过程]]"
  - "[[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]"
  - "[[Clippings/articles/Obsidian 的 13 种内容形式.md]]"
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

## 2025-2026 重要更新 | 2026-07-05

> — [[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]

- **Bases**：原生数据库视图，读 YAML 元数据，与 Properties 深度整合
- **Canvas 增强**：支持反向链接，可嵌入看板
- **AI 深度融合**：可通过 Ollama 实现完全本地的私有智能知识库

## 推荐插件矩阵（20个）| 2026-07-05

> — [[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]

| 类别 | 插件 | 核心功能 |
|------|------|---------|
| **数据查询** | Dataview | DQL 语法跨笔记查询 YAML 元数据，生成动态表格/列表 |
| | Omnisearch | 智能全文搜索，支持 OCR & PDF，权重算法排序 |
| **自动化模板** | Templater | 可编程模板引擎，支持 JS、系统命令、动态日期 |
| | QuickAdd | 工作流胶水：快速捕获、模板创建、链式宏执行 |
| | Linter | 保存时自动统一 Markdown 格式、YAML 排序 |
| **任务管理** | Tasks | 跨笔记任务管理，截止日期、循环、优先级 |
| | Kanban | 可视化看板（Markdown 存储） |
| | Calendar + Periodic Notes | 月视图日历 + 周/月/季/年笔记 |
| **可视化** | Excalidraw | 手绘白板，元素可链接笔记（570万+下载） |
| **导航增强** | Various Complements | IDE 级自动补全，无需 [[ 即可建议链接 |
| | Commander | 常用命令添加至界面各处 |
| | Note Toolbar | 上下文感知工具栏 |
| **AI 集成** | Smart Connections | 本地 AI 嵌入，侧边栏自动显示语义相关笔记 |
| | Obsidian Copilot | 基于 RAG 的本地 AI 对话（Ollama + llama3.2） |
| | Text Generator | 连接多模型，辅助写作、摘要、翻译 |
| **版本控制** | Git | 10分钟自动提交，完整差异对比 |
| | BRAT | 直接从 GitHub 安装/更新 Beta 插件 |
| **界面** | Style Settings | 图形化调整主题变量（搭配 Minimal 主题） |
| | Supercharged Links | 基于元数据给链接添加颜色/emoji 前缀 |
| | Meta Bind | 笔记内嵌入交互组件（滑块、开关、按钮） |

### 5周渐进安装计划

- **第1周**：Templater, Calendar+Periodic Notes, Linter, Git
- **第2周**：Dataview, Tasks, QuickAdd, Various Complements
- **第3周**：Commander, Style Settings, Omnisearch, Note Toolbar
- **第4周**：Excalidraw, Kanban, Meta Bind, BRAT, Supercharged Links
- **第5周（按需）**：Smart Connections, Copilot, Text Generator

> — [[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]], L120-200

## 13种内容形式与取舍指南 | 2026-07-30

基于实战经验，对 Obsidian 13 种内容形式的取舍建议：

### 推荐使用（标准 Markdown）

**文本格式**：只用粗体、斜体、高亮，减少其他格式以避免导出异常。可通过主题 CSS 给不同格式赋不同颜色。

**无序列表** `-`：分类和集合的首选，灵活不绑定顺序。

**代码块**：必须标注语言名（如 ` ```python `），否则无语法高亮。

**表格**：并排对比信息的唯一选择，虽编辑体验一般但无可替代。`:---` 左对齐，`:---:` 居中，`---:` 右对齐。

**脚注** `[^1]`：一句话说不完的补充、来源、延伸阅读全部放脚注，正文只留主线。Obsidian 支持悬停预览和侧边栏脚注视图。

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L28-35, L80-85, L88-95, L120-126

### 谨慎使用（Obsidian 扩展）

**内部链接 `[[笔记名]]`**：核心能力，但注意只在 Obsidian 内部操作重命名时才自动更新，外部（Finder/终端）操作则失效。块引用 `^块id` 脆弱，段落重新编辑可能导致 ID 变更。嵌入适合稳定不变的内容。

**图片 `![[图片.png|400]]`**：利用全局索引，笔记移动不影响路径。

**任务列表 `- [ ]`**：配合 Tasks 插件或 Dataview 可跨文件聚合待办，变成"可查询的待办信号"。

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L102-117, L128-134, L40-47

### 不推荐（锁定生态）

**Callout `> [!tip]`**：会锁定在 Obsidian 生态，切换到 Typora、VS Code 等会显示源码符号，破坏可移植性。坚持用标准 `>`。

**HTML 嵌入**：一旦开始写 HTML 就放弃可移植性。唯一场景：`<center>` 居中、`<details><summary>` 折叠块。

**Mermaid**：仅适合不超过 5 个节点的简单流程，中文常乱码。复杂图用 Excalidraw 画完截图粘贴。

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L50-55, L140-147, L138-143

### 选择原则

**结构重于样式**。选择内容形式时优先考虑：可移植性 > 可搜索性 > 可维护性 > 样式表现。

> — [[Clippings/articles/Obsidian 的 13 种内容形式.md]], L155-166

## 参见

- [[concepts/Obsidian 四层架构]]
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
- [[Clippings/articles/Obsidian 的 13 种内容形式.md]]