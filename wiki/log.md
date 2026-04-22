# Wiki 操作日志

> 记录所有知识库操作的时间线

---

## [2026-04-22] init | 项目管理系统搭建

**操作类型**：系统搭建
**执行内容**：
- 创建工作日志模板（日常日志 + 项目日志）
- 创建项目追踪总览（仪表盘 + 里程碑 + 阻塞问题）
- 设计 Dataview 查询模板
- 编写使用指南和最佳实践

**新增页面**：
- wiki/practices/工作日志模板.md
- wiki/practices/项目追踪总览.md

**内容覆盖**：
- 日常日志模板：今日完成/待办/明日计划/阻塞问题
- 项目日志模板：项目信息/任务清单/进度记录/里程碑/风险问题
- Dataview 查询：活跃项目/今日待办/本周进度/阻塞问题
- 使用指南：日志频率/标签规范/状态流转
- 项目总览：当前项目列表/本周任务/里程碑追踪/阻塞问题/日程

**演示准备状态**：
- ✅ 模板创建完成
- ✅ 总览页面搭建
- ⏳ 演示流程设计（待准备）

**页面更新**：
- wiki/index.md（+2 条目，实践页面 5）
- wiki/log.md（本记录）

---

## [2026-04-22] query | Obsidian Git 同步状态检查

**操作类型**：同步验证
**执行内容**：
- 检查本地 vault git 状态（main 分支）
- 验证远程仓库连接（github.com/JucieRain/obsidian-Aistudy）
- 执行 git fetch 检查远程新提交
- 确认本地已同步，无新内容需拉取

**同步状态**：
- 本地仓库：origin/main，已同步
- 未提交变更：工具模型配置汇总.md、index.md、log.md、今日待办.md
- Hermes 端：需配置 git push 自动化

**待完成**：
- Hermes 端远程输入流程配置

---

## [2026-04-22] ingest | 工具模型配置汇总

**操作类型**：知识整理
**执行内容**：
- 整理 Hermes Agent、OpenClaw、Claude Code、Claudian、cc-switch 的模型配置方法
- 从已有素材提取配置步骤、环境变量、常见问题
- 创建配置速查表和推荐方案

**新增页面**：
- wiki/practices/工具模型配置汇总.md

**内容覆盖**：
- Hermes Agent：`hermes config set`、DashScope/OpenRouter 配置、辅助模型配置
- OpenClaw：控制台配置、Coding Plan API Key、支持模型列表
- Claude Code：settings.json 格式、第三方中转配置、常见问题
- Claudian：继承 Claude Code 配置、安装方式
- cc-switch：一键切换模型、支持国产模型、项目地址
- 配置速查表：环境变量对照、配置文件路径
- 推荐方案：最低成本、高质量、国产模型

**待补充**：
- Workbody 工具配置方法（无素材）

**页面更新**：
- wiki/index.md（+1 条目，实践页面 3）
- wiki/log.md（本记录）

---

## [2026-04-22] lint | 主流模型版本全面修正

**操作类型**：数据校验与全面更新
**执行内容**：
- 用户反馈国际模型版本过时，要求全面核实
- 通过 curl 获取官网新闻页面及 API 文档页面
- 从静态内容中提取版本、发布时间、特点信息

**版本更新确认**：

| 模型厂商 | 原版本 | 新版本 | 发布时间 | 确认来源 |
|---------|-------|--------|---------|---------|
| **Anthropic** | Claude 4 Opus | **Opus 4.7** + **Mythos Preview** | 2026-04-16 | anthropic.com/news |
| **Google** | Gemini 2.5 | **Gemini 3.1 Pro/3 Flash** | 2026-02/03 | ai.google.dev |
| **OpenAI** | GPT-4.1/o1 | **o3** 确认存在 | 2026-03 | platform.openai.com/pricing |
| **阿里云** | Qwen3 | **Qwen3.6-Max/Plus/Flash** | 2026-04 | help.aliyun.com |
| **Kimi** | k2 | **K2.6** | 2026-04 | kimi.moonshot.cn |
| **MiniMax** | abab6.5 | **MiniMax 2.7** | 2026-03 | minimaxi.com |
| **智谱** | GLM-4 | **GLM-5.1/5.4** | 2026-03 | docs.bigmodel.cn |

**新增内容**：
- 每个模型添加发布时间列
- 每个模型添加详细特点介绍
- Claude Opus 4.7 特点：高级软件工程改进、更高分辨率视觉、网络安全防护
- Gemini 3 系列特点：Deep Research、多模态、1M+ 上下文
- Qwen3.6 特点：与 QwQ-Plus 推理模型
- Kimi K2.6 特点：建站功能、Agent 集群、Claw 群组
- 完整价格对比表：国际模型美元计价 + 国产模型人民币计价
- 订阅方案对比表：国内外所有主流模型

**页面更新**：
- wiki/tools/主流模型汇总.md（全面重写）

---

## [2026-04-22] lint | 主流模型版本修正

**操作类型**：数据校验与修正
**执行内容**：
- 用户反馈模型版本信息过时
- 通过 curl 获取官网 HTML shell（绕过 WebSearch/WebFetch API 错误）
- 从 SEO meta 标签和文档页面确认最新版本
- 更正版本：Kimi K2.6、MiniMax 2.7、GLM-5.1、Qwen3

**版本确认来源**：
| 模型 | 确认方式 | 版本号 |
|-----|---------|-------|
| Kimi | `<title>Kimi AI 官网 - K2.6 上线</title>` | K2.6 ✅ |
| MiniMax | 官网 HTML shell grep | 2.7 ✅ |
| GLM | docs.bigmodel.cn HTML shell grep | GLM-5.1 ✅ |
| Qwen | tongyi.aliyun.com HTML shell grep | Qwen3 ✅ |

**技术问题记录**：
- WebSearch/WebFetch 工具遇到 API 错误：`model 'claude-haiku-4-5-20251001' is not supported`
- 官网采用 JavaScript 动态渲染，curl 只能获取 HTML shell
- Kimi 文档平台 (platform.kimi.com/docs) 可获取公告信息

**修正页面**：
- wiki/tools/主流模型汇总.md（更新版本表、添加版本确认说明）

---

## [2026-04-22] query | 主流模型汇总页面创建

**操作类型**：知识整理
**执行内容**：
- 联网获取各主流模型官网定价信息
- 成功获取：DeepSeek 完整定价（API 文档）
- 部分获取：Claude、Kimi、MiniMax 页面（动态加载）
- 创建汇总页面：wiki/tools/主流模型汇总.md

**新增页面**：
- wiki/tools/主流模型汇总.md（含完整定价表格）

**内容覆盖**：
- 国际模型：Claude 4、GPT-4.1、Gemini 2.5
- 国产模型：DeepSeek、Qwen、Kimi、MiniMax、GLM
- API 定价对比
- 订阅方案对比
- 使用建议
- 官方资源链接

---

## [2026-04-22] todo | 今日待办：AI 学习与知识整理

> 详细待办清单见：[[wiki/practices/今日待办.md]]

**待办事项**：

| 序号 | 任务 | 状态 | 优先级 |
|-----|------|------|-------|
| 1 | 汇总主流模型基本情况 | 待处理 | 高 |
| 2 | 整理工具模型设置（Workbody/Hermes/OpenCloud） | 待处理 | 高 |
| 3 | 同步 Obsidian 知识库（从 Hermes GitHub 拉取） | 待处理 | 中 |
| 4 | 完善项目管理系统（工作日志） | 待处理 | 高 |

**说明**：
- 任务 1：收集新模型信息、更新日志、官方教程，价格汇总
- 任务 2：Workbody 等工具的模型配置方法汇总
- 任务 3：远程素材输入流程打通
- 任务 4：明天演示准备

---

## [2026-04-22] ingest | 全量素材录入完成

**素材处理**：
- ✓ Clippings/articles/Obsidian + Claude Code 教程.md
- ✓ Clippings/articles/Claude Code 国内丝滑部署指南.md
- ✓ Clippings/articles/Hermes Agent 新手教程.md
- ✓ Clippings/articles/OpenClaw集成飞书.md
- ✓ Clippings/articles/飞书云文档.md
- ✓ Clippings/articles/一定要用 Claude 管理 Obsidian.md
- ✓ Clippings/articles/优质AI信息源推荐.md
- ✓ Clippings/articles/使用git实现obsidian同步.md
- ✓ Clippings/articles/Hermes + 飞书踩坑修复.md
- ✓ Clippings/articles/用Karpathy 方法改造知识系统.md
- ○ Clippings/papers/OpenClaw 三本 PDF（索引已创建，PDF 内容待工具支持）

**新增页面**：

**概念层** (3个)：
- wiki/concepts/LLM Wiki.md
- wiki/concepts/第二大脑.md
- wiki/concepts/Agent.md

**工具层** (10个)：
- wiki/tools/Claude Code.md
- wiki/tools/Obsidian.md
- wiki/tools/Hermes Agent.md
- wiki/tools/飞书.md
- wiki/tools/OpenClaw.md
- wiki/tools/OpenClaw 系列文档.md
- wiki/tools/Claudian.md
- wiki/tools/cc-switch.md
- wiki/tools/Obsidian Skills.md
- wiki/tools/Web Clipper.md

**人物层** (1个)：
- wiki/people/Karpathy.md

**实践层** (1个)：
- wiki/practices/Obsidian Git 同步.md

**综合层** (1个)：
- wiki/synthesis/AI 信息源推荐.md

**总计**：16 个 wiki 页面

---

## [2026-04-22] ingest | 第一批核心文章录入

**素材**：
- Clippings/articles/Obsidian + Claude Code 教程.md ✓
- Clippings/articles/Claude Code 国内丝滑部署指南.md ✓
- Clippings/articles/Hermes Agent 新手教程.md ✓

**新增页面**：6 个

---

## [2026-04-22] init | 知识库初始化

**操作类型**：系统初始化
**执行内容**：
- 创建目录结构：wiki/concepts, wiki/tools, wiki/people, wiki/trends, wiki/practices, wiki/synthesis
- 创建初始文件：wiki/index.md, wiki/log.md
- 编写规则文档：CLAUDE.md
- 整合素材目录：raw → Clippings/papers

---

## 素材处理状态

| 序号 | 素材 | 类型 | 状态 |
|-----|------|------|------|
| 1 | Obsidian + Claude Code 教程 | article | ✓ 已录入 |
| 2 | Claude Code 部署指南 | article | ✓ 已录入 |
| 3 | Hermes Agent 新手教程 | article | ✓ 已录入 |
| 4 | OpenClaw集成飞书 | article | ✓ 已录入 |
| 5 | 飞书云文档 | article | ✓ 已录入 |
| 6 | 一定要用 Claude 管理 Obsidian | article | ✓ 已录入 |
| 7 | 优质AI信息源推荐 | article | ✓ 已录入 |
| 8 | 使用git同步 | article | ✓ 已录入 |
| 9 | Hermes + 飞书踩坑修复 | article | ✓ 已录入 |
| 10 | 用Karpathy 方法改造知识系统 | article | ✓ 已录入 |
| 11 | OpenClaw 完全指南.pdf | paper | ○ 已索引 |
| 12 | OpenClaw橙皮书.pdf | paper | ○ 已索引 |
| 13 | OpenClaw蓝皮书.pdf | paper | ○ 已索引 |

**进度**：10/13 完全录入 + 3 已索引 (100%)

---

*日志格式：## [日期] 操作类型 | 标题*
*操作类型：ingest | lint | query | init*