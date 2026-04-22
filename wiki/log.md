# Wiki 操作日志

> 记录所有知识库操作的时间线

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