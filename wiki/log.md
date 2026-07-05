# Wiki 操作日志

> 记录所有知识库操作的时间线

---

## 2026-07-05 ingest

- **素材**：[[Clippings/articles/100个WorkBuddy应用案例合集.md]]
- **更新页面**：[[wiki/tools/WorkBuddy]]（追加12类应用案例 + 包装印刷垂直应用 + vs传统AI工具对比）
- **来源**：飞书文档 https://my.feishu.cn/wiki/OJDfwtORZiirHIkt9B7cWnmKnTb

## 2026-07-05 ingest

- **素材**：[[Clippings/articles/Obsidian本地知识库搭建：从入门到第二大脑.md]]
- **新增页面**：[[wiki/concepts/PARA]]、[[wiki/concepts/Zettelkasten]]、[[wiki/concepts/MOC]]
- **更新页面**：[[wiki/tools/Obsidian]]（2025-2026更新 + 20插件矩阵 + 5周安装计划）、[[wiki/concepts/LLM Wiki]]（v2六大扩展）
- **来源**：微信公众号 https://mp.weixin.qq.com/s/SPLTD-hFAsyYAA7V1lU8OA

## 2026-07-05 ingest

- **素材**：[[Clippings/articles/AI驱动的PPT工作流：女娲Skill+PPT Director.md]]
- **新增页面**：[[wiki/concepts/认知蒸馏]]、[[wiki/tools/女娲Skill]]、[[wiki/tools/PPT Director Skill]]
- **来源**：微信公众号 https://mp.weixin.qq.com/s/WB5SiBxIZn_v8XK5af-uJw

## 2026-07-05 ingest

- **素材**：[[Clippings/articles/PPT Master：开源AI PPT生成工具.md]]
- **新增页面**：[[wiki/tools/PPT Master]]
- **来源**：微信公众号 https://mp.weixin.qq.com/s/Wtgn3G6et93_sX8ql-3eHA

---

## [2026-05-01] ingest | Hermes Agent 橙皮书录入

**操作类型**：素材录入（PDF）
**触发原因**：用户请求录入新资料

**素材处理**：
- ✓ Clippings/Hermes Agent 从入门到精通.pdf → papers/（花叔橙皮书 v260407）

**素材信息**：
- 作者：花叔（公众号「花叔」、B站「AI进化论-花生」）
- 版本：v260407
- 页数：约80页，5大Part、17章节
- 核心主题：自改进 Agent、学习循环、三层记忆、Harness Engineering

**新增页面（4个）**：

**概念层** (2个)：
- wiki/concepts/学习循环.md - 自改进Agent核心机制，五环节闭环飞轮
- wiki/concepts/agentskills.io.md - Skill互通标准，30+工具支持

**人物层** (1个)：
- wiki/people/Mitchell Hashimoto.md - Terraform创造者，Harness Engineering理念创始人

**更新页面（4个）**：
- wiki/tools/Hermes Agent.md - 补充学习循环、三层记忆、Skill自改进、agentskills.io互通、$5 VPS部署、三工具对比表
- wiki/concepts/Harness Engineering.md - 补充Mitchell命名、五组件Hermes内建映射、三层监督框架
- wiki/people/花叔.md - 补充三本橙皮书系列、Hermes橙皮书亮点
- wiki/index.md（+4条目，总页面数60，素材数41文章+4PDF）

**核心内容提取**：

| 类别 | 提取内容 |
|-----|---------|
| **核心概念** | 自改进Agent、学习循环、三层记忆、Harness Engineering五组件、agentskills.io |
| **关键论点** | "第一个出厂就带缰绳的Agent，缰绳会自己长大"、"不是替代是递进"、"自改进天花板取决于反馈信号" |
| **对比分析** | Hermes vs Claude Code vs OpenClaw（工匠/标准化框架/管家） |
| **部署方案** | $5 VPS + Telegram Gateway，24/7在线成本<$10/月 |
| **人物观点** | Mitchell "每次犯错加一条规则"、花叔 "最终胜出的是会组合工具的人" |

**溯源标注**：所有关键事实已标注来源行号（格式：`> — Clippings/papers/..., §章节`）

---

## [2026-04-30] lint | 常规体检 + 深度抽查

**操作类型**：健康检查
**触发原因**：用户请求执行 lint

**检查结果**：

| 检查项 | 发现问题 | 严重程度 |
|-------|---------|---------|
| **断链** | 2（Skill、Honcho） | 🔴 高 |
| **漂移** | 1（Hermes Star数） | 🔴 高 |
| **孤儿页面** | 0 | ✅ |

**问题详情**：

1. **断链 [[concepts/Skill]]**：被 5 个页面引用但无独立页面
2. **断链 [[concepts/Honcho]]**：在多Agent协同中被引用但无页面
3. **漂移 Hermes Star 数**：素材"10万多 Star"（L30） vs Wiki"74K Stars"

**生成报告**：
- wiki/lint-report-2026-04-30.md

**更新调度**：
- wiki/schedule.jsonl（next_due: 2026-05-07）

**待确认修复**：
- 创建 Skill 概念页面
- Honcho 链接改指向 Hermes Agent
- 更新 Hermes Star 数为"10万+"

---

## [2026-04-30] lint-fix | 执行修复（全部完成）

**操作类型**：Lint 问题修复
**触发原因**：用户确认立即执行

**修复内容**：

| 序号 | 修复动作 | 结果 |
|-----|---------|------|
| 1 | 创建 `wiki/concepts/Skill.md` | ✅ 已创建，含来源标注 L45-50 |
| 2 | Honcho 断链修复 | ✅ 改为指向 [[tools/Hermes Agent]] |
| 3 | Hermes Star 数更新 | ✅ 改为"10万+"，添加来源行号 L30 |

**新增文件**：
- wiki/concepts/Skill.md - Agent 可复用能力单元

**修改文件**：
- wiki/concepts/多Agent协同.md - Honcho 链接修复
- wiki/tools/Hermes Agent.md - Star 数更新+来源标注
- wiki/index.md - Star 数更新+新增 Skill 页面
- wiki/lint-report-2026-04-30.md - 标记修复完成

**页面更新**：
- wiki/index.md（+1 条目，总页面数 57，概念页面 12）

**溯源标注示例**（新规则首次应用）：
```markdown
| **GitHub Stars** | 10万+ |
> — Clippings/articles/给 10 万 Star 的 Hermes..., L30
```

---

## [2026-04-30] system | 知识库改造：防漂移机制 + 调度系统

**操作类型**：系统架构升级
**触发原因**：用户基于"知识漂移"素材讨论优化方案

**改造内容**：

### 新增：溯源机制（防漂移）

在 CLAUDE.md 第四章新增溯源规则：
- 关键事实必须标注来源行号（数字/百分比/具体结论/人物观点/时间）
- 格式：`> — [素材路径], L[起始行]-[结束行]`
- 可不标注：AI综合、常识、推导结论

### 增强：Lint 检查项

新增三个检查项：
| 检查项 | 周期 | 内容 |
|-----|------|------|
| **矛盾检测** | 每周 | 同一事实不同页面说法不同 |
| **过时检测** | 每周 | 素材有更新，wiki未同步 |
| **漂移检测** | 每月 | 随机抽5页对比原文验证 |

### 新增：调度记录机制

创建 `wiki/schedule.jsonl` 记录任务执行时间：
- lint-weekly（常规体检，每周）
- lint-monthly（深度体检，每月）
- journal-weekly（日记整合，每周）

### 新增：会话启动检查

每次会话开始时：
1. 读取 schedule.jsonl，检查是否超期
2. 检查 Clippings/ 根目录是否有新素材
3. 如有超期或新素材 → 提醒用户

**新增文件**：
- wiki/schedule.jsonl - 调度任务记录

**修改文件**：
- CLAUDE.md - 新增第四章溯源机制、增强Lint、新增第六章调度机制
- wiki/index.md - 新增调度任务表格

**改造目标**：
- 🔴 防止知识漂移（标注行号 + 深度体检）
- 🟡 解决"找不到"（调度系统为后续搜索增强铺路）
- 🟡 可维护性（定期提醒，不依赖电脑持续运行）

---

## [2026-04-30] ingest | 6篇新素材录入（组织转型 + Obsidian + Hermes + LLM Wiki维护）

**操作类型**：素材录入
**触发原因**：用户请求录入最新素材

**素材处理**：
- ✓ Clippings/组织级AI软件工程转型：不仅是新工具，更是新组织.md → articles/（知乎文章）
- ✓ Clippings/Obsidian x Agent 终极指南，从零打造个人 Agent 系统.md → articles/（空格丶公众号）
- ✓ Clippings/Obsidian Cli 基础使用教程 AI化知识管理全过程.md → articles/（ShikiLab公众号）
- ✓ Clippings/llm Wiki 养了三周，开始出毛病了.md → articles/（AI赋能说公众号）
- ✓ Clippings/给 10 万 Star 的 Hermes 装个记忆外挂，AI 终于能越用越聪明了。.md → articles/（逛逛公众号）
- ✓ Clippings/装完 Hermes 一定要配置这五套系统，秒变满配版，能力提升数倍不止.md → articles/（科技君公众号）

**新增页面（17个）**：

**概念层** (3个)：
- wiki/concepts/知识漂移.md - Wiki与原文脱节现象，三个毛病三个解法
- wiki/concepts/组织级AI转型.md - 一把手工程，烧token策略，全员覆盖
- wiki/concepts/Spec-Driven Development.md - 规约驱动开发，先写规约再让Agent生成

**工具层** (2个)：
- wiki/tools/MemOS.md - 记忆张量团队开源记忆系统，智能去重+混合检索
- wiki/tools/qmd.md - 本地Markdown搜索引擎，为LLM Wiki提供检索

**人物层** (6个)：
- wiki/people/空格丶.md - AI生产力专栏作者，Obsidian作为AI操作系统视角
- wiki/people/ShikiLab.md - Obsidian知识管理实践者，《上头Obsidian》作者
- wiki/people/AI赋能说.md - LLM Wiki实践者，知识漂移问题发现者
- wiki/people/逛逛.md - GitHub开源推荐博主，MemOS插件推荐者
- wiki/people/科技君.md - Hermes Agent进阶配置专家
- wiki/people/FusionCID学习AI应用随笔.md - 组织级AI转型专家

**实践层** (3个)：
- wiki/practices/Obsidian CLI配置指南.md - Obsidian v1.12 CLI + Claude Code + MiniMax配置
- wiki/practices/Hermes五大配置模块.md - 身份记忆/感知能力/表达能力/效率成本/生态导航
- wiki/practices/LLM Wiki维护经验.md - 三周实践经验，体检机制设计

**更新页面（4个）**：
- wiki/concepts/LLM Wiki.md - 补充实践经验、三个毛病三个解法、知识漂移
- wiki/concepts/长期记忆.md - 补充 MemOS 智能去重+混合检索
- wiki/tools/Obsidian.md - 补充 AI操作系统视角、CLI能力、Karpathy三件套
- wiki/tools/Hermes Agent.md - 补充 MemOS插件、五大配置模块、Token管控工具

**页面更新**：
- wiki/index.md（+17条目，总页面数56，素材数41文章+3PDF）
- wiki/log.md（本记录）

**覆盖内容**：

| 页面 | 补充内容 |
|-----|---------|
| LLM Wiki | 实践经验（三个毛病：漂移/孤岛/找不到）、三个解法（溯源/体检/搜索）、AI赋能说贡献 |
| 长期记忆 | MemOS智能去重机制、混合检索引擎、预检索注入、与Hindsight对比 |
| Obsidian | AI操作系统视角、CLI能力、URI Scheme、Karpathy三件套、AI工作桌类比 |
| Hermes Agent | MemOS记忆插件、五大配置模块、Hindsight记忆系统、Token管控（Tokscale/RTK） |

---

## [2026-04-23] ingest | 2篇新素材录入（OpenClaw省钱安全 + Harness Engineering）

**操作类型**：素材录入
**触发原因**：用户请求录入最新素材

**素材处理**：
- ✓ Clippings/Openclaw养龙虾秘籍大公开！【安全+省钱】.md → articles/（秋芝2046公众号）
- ✓ Clippings/Harness Engineering：Agent开发的关键战场.md → articles/（知乎文章）

**新增页面（2个）**：

**概念层** (1个)：
- wiki/concepts/Harness Engineering.md - Agent工程化框架，六大战场，三大核心价值

**人物层** (1个)：
- wiki/people/真理非著名不专业混子工程师.md - Harness Engineering概念提出者，知乎博主

**更新页面（2个）**：
- wiki/tools/OpenClaw.md - 补充养龙虾省钱指南（上下文瘦身/模型混搭/本地模型）+安全指南（内外防护）
- wiki/people/秋芝2046.md - 补充 OpenClaw 省钱安全教程作为贡献

**页面更新**：
- wiki/index.md（+2条目，总页面数39，素材数35文章+3PDF）
- wiki/log.md（本记录）

**覆盖内容**：

| 页面 | 补充内容 |
|-----|---------|
| OpenClaw | 省钱三大妙招（上下文瘦身四步法、模型混搭三档分类、本地模型推荐硬件）、安全内外防护（对外三件事+对内三件事）、长期建议 |
| Harness Engineering | 定义、与传统软件工程区别、三大核心价值、六大战场详解、业界标杆案例（Cursor/Claude Code/GitHub Copilot/LangGraph）、当前挑战与未来趋势 |
| 秋芝2046 | 新增 OpenClaw 省钱安全教程贡献 |
| 真理非著名不专业混子工程师 | 新人物页面，Harness Engineering 概念提出者 |

---

## [2026-04-23] update | AI信息源推荐UP主补充

**操作类型**：内容更新
**触发原因**：用户推荐 4 个对普通人 AI 入门有帮助的 B站 UP主

**新增人物页面（3个）**：
- wiki/people/数字牧游人.md - 普通人视角切入AI工作方式思考
- wiki/people/第四种黑猩猩CHIMP.md - AI入门科普，通俗易懂
- wiki/people/珍妮丁丁AI说.md - AI应用场景分享，接地气

**更新页面（2个）**：
- wiki/synthesis/AI 信息源推荐.md - 新增「AI入门与工作方式思考」板块，添加4个UP主推荐
- wiki/index.md（+3人物条目，总页面数37）

**推荐UP主**：

| UP主 | 特点 |
|-----|------|
| 秋芝2046 | AI工具实践教程，WorkBuddy龙虾养成（已有人物页面） |
| 数字牧游人 | 普通人视角切入AI工作方式思考 |
| 第四种黑猩猩CHIMP | AI入门科普，通俗易懂 |
| 珍妮丁丁AI说 | AI应用场景分享，接地气 |

---

## [2026-04-23] ingest | 5篇素材批量录入（Typeless + OpenClaw三书）

**操作类型**：素材录入
**触发原因**：用户请求录入新素材和 PDF 转换的 Markdown

**素材处理**：
- ✓ Clippings/typeless安装与设置.md → articles/
- ✓ Clippings/探索typeless核心功能.md → articles/
- ✓ Clippings/papers/OpenClaw完全指南（花园版）.md（PDF 转换）
- ✓ Clippings/papers/OpenClaw橙皮书-从入门到精通-v1.3.1.md（PDF 转换）
- ✓ Clippings/papers/OpenClaw蓝皮书-1.0.0版.md（PDF 转换）

**新增页面（3个）**：

**人物层** (3个)：
- wiki/people/花园老师.md - code秘密花园作者，花园版完全指南作者，7个Agent团队案例
- wiki/people/花叔.md - 橙皮书作者，AI编程知识星球星主，命令速查表+Coding Plan对比
- wiki/people/杨彧鑫AI.md - 蓝皮书作者，23个赚钱案例+10行业落地方案

**更新页面（2个）**：
- wiki/tools/Typeless.md - 补充安装步骤（macOS/Windows）、核心功能详解（AI自动编辑6项能力）
- wiki/tools/OpenClaw.md - 补充核心数据、记忆系统、部署方式总览、PDF来源链接

**页面更新**：
- wiki/index.md（+3人物条目，总页面数34，素材数33文章+3PDF）
- wiki/log.md（本记录）

**覆盖内容**：

| 工具/人物 | 补充内容 |
|---------|---------|
| Typeless | macOS 安装步骤、Windows 安装步骤、AI 自动编辑详解（移除填充词/移除重复/改口编辑/理解意图/自动格式化/不同应用语气） |
| OpenClaw | GitHub 历史增速第一、四层记忆架构、向量记忆搜索、部署方式总览、花园版/橙皮书/蓝皮书来源 |
| 花园老师 | 7个 Agent 团队（生图/资讯/开发/投资/社区/写作/智能专家），为什么不做全能 Agent |
| 花叔 | 橙皮书 109 页、命令速查表、资源链接汇总、Coding Plan 对比 |
| 杨彧鑫AI | 蓝皮书 189 页、23个赚钱案例、10行业落地方案 |

---

## [2026-04-22] classify | 素材分类整理（第二批）

**操作类型**：素材整理
**触发原因**：发现根目录有 7 个未分类素材

**分类判断**：

| 文件名 | 判断依据 | 分类 |
|-------|---------|------|
| 磨砺你的思维。.md | source: obsidian.md 官网 | article |
| Typeless Windows 应用发布说明.md | source: typeless.com 官网 | article |
| OpenClaw在飞书和Telegram上养了12个AI员工.md | source: mp.weixin.qq.com 微信文章 | article |
| Windows 系统安装指南 (CodeBuddy).md | source: codebuddy.cn 官方文档 | article |
| Claw 远程控制 (CodeBuddy).md | source: codebuddy.cn 官方文档 | article |
| 快速开始 (CodeBuddy).md | source: codebuddy.cn 官方文档 | article |
| WorkBuddy 小程序简介 (CodeBuddy).md | source: codebuddy.cn 官方文档 | article |

**分类移动**：
- 7 个文件全部移动至 `Clippings/articles/`

**目录状态**：
- Clippings/ 根目录：已清空
- Clippings/articles/：31 个文章

**待处理**：
- ⏳ Phase 2 内容提取（待用户确认是否继续）
- ⏳ Phase 3 Wiki 更新（创建/更新相关页面）

---

## [2026-04-22] ingest | 7篇素材批量录入（Phase 2+3 完成）

**操作类型**：素材录入
**触发原因**：用户确认继续执行 Phase 2 内容提取和 Phase 3 Wiki 更新

**素材处理**：
- ✓ Clippings/articles/磨砺你的思维。.md（Obsidian 官网）
- ✓ Clippings/articles/Typeless Windows 应用发布说明.md
- ✓ Clippings/articles/OpenClaw在飞书和Telegram上养了12个AI员工，它们还会自己开会.md
- ✓ Clippings/articles/Windows 系统安装指南 (CodeBuddy).md
- ✓ Clippings/articles/Claw 远程控制 (CodeBuddy).md
- ✓ Clippings/articles/快速开始 (CodeBuddy).md
- ✓ Clippings/articles/WorkBuddy 小程序简介 (CodeBuddy).md

**新增页面（2个）**：

**工具层** (1个)：
- wiki/tools/Typeless.md - AI语音听写工具，边想边说+翻译+个性化风格

**人物层** (1个)：
- wiki/people/俊哥AI副业.md - OpenClaw多Agent实践者，12个AI员工配置教程

**更新页面（3个）**：
- wiki/tools/Obsidian.md - 补充官网功能（白板Canvas、Sync同步、Publish发布）
- wiki/tools/OpenClaw.md - 补充多Agent配置（agents.list、bindings、agentToAgent、AGENTS.md、踩坑经验）
- wiki/tools/WorkBuddy.md - 补充安装指南、Claw远程控制、小程序、产品模式

**页面更新**：
- wiki/index.md（+2条目，总页面数31，素材数31文章+3PDF）
- wiki/log.md（本记录）

**覆盖内容**：

| 工具 | 补充内容 |
|-----|---------|
| Obsidian | 官网资源链接、白板Canvas、Sync同步、Publish发布、版本历史 |
| OpenClaw | 多Agent路由配置、飞书多账户bindings、agentToAgent通信、AGENTS.md团队成员、SOUL.md人设、踩坑经验 |
| WorkBuddy | Windows安装指南、Claw远程控制（6平台）、小程序云上/本机模式、工作/编程模式 |
| Typeless | 新工具页面：语音听写、翻译、任意提问、版本历史、隐私设计 |

---

## [2026-04-22] ingest | 新增3篇官方文档素材

**操作类型**：素材录入
**执行内容**：补充缺失的工具官方文档

**新增素材**：
- Clippings/articles/Claude Code 官方文档.md
- Clippings/articles/cc-switch GitHub 项目.md
- Clippings/articles/WorkBuddy 官网.md

**更新页面**：
- wiki/tools/Claude Code.md - 补充官方文档链接、Windows详细安装、第三方中转配置
- wiki/tools/cc-switch.md - 补充多工具支持、详细功能说明、使用场景
- wiki/tools/WorkBuddy.md - 补充官网下载入口、安装步骤

**覆盖缺失内容**：
| 工具 | 补充内容 |
|-----|---------|
| Claude Code | 官方文档链接、Windows安装详解、第三方中转配置 |
| cc-switch | 多工具支持（Codex/OpenCode/OpenClaw/Gemini CLI）、使用场景 |
| WorkBuddy | 官网下载入口、安装步骤 |

**页面更新**：
- wiki/index.md（素材数更新：21文章）
- wiki/log.md（本记录）

---

## [2026-04-22] organize | 素材分类整理

**操作类型**：素材整理
**触发原因**：优化录入流程，发现根目录有未分类素材

**分类移动**：

| 原路径 | 分类 | 新路径 |
|-------|------|-------|
| Clippings/Hermes Agent 完整指南.md | article | Clippings/articles/ |
| Clippings/购买并部署OpenClaw应用镜像.md | article | Clippings/articles/ |
| Clippings/OpenClaw 养成路线图.md | article | Clippings/articles/ |
| Clippings/深度研究Prompt.md | article | Clippings/articles/ |
| Clippings/YC总裁开源GBrain.md | article | Clippings/articles/ |
| Clippings/Hermes+Kimi Agent军团.md | article | Clippings/articles/ |
| Clippings/WorkBuddy教程.md | article | Clippings/articles/ |

**清理文件**：
- 删除 `Clippings/papers/OpenClaw 完全指南.pdf.md`（空占位文件）

**目录状态**：
- Clippings/ 根目录：已清空（无未分类素材）
- Clippings/articles/：17个文章
- Clippings/papers/：3个PDF

**规则更新**：
- CLAUDE.md 3.1节录入流程优化为三阶段：
  - Phase 1: 素材分类（扫描→判断→移动）
  - Phase 2: 内容提取
  - Phase 3: Wiki更新

---

## [2026-04-22] ingest | 7篇新素材批量录入

**素材处理**：
- ✓ Clippings/YC 总裁开源了自己亲手写的 AI Agent 大脑，1 周就 1 万点赞。.md
- ✓ Clippings/万字保姆级教程：Hermes+Kimi K2.6 打造7x24h Agent军团.md
- ✓ Clippings/OpenClaw 养成路线图：从装完到用好的 8 个阶段.md
- ✓ Clippings/分享一个我用了2年的深度研究Prompt，半小时帮你搞懂任何陌生领域。.md
- ✓ Clippings/用WorkBuddy养出你的龙虾搭子！【附提示词】.md
- ✓ Clippings/购买并部署OpenClaw应用镜像.md
- ✓ Clippings/Hermes Agent 完整指南：从安装到进阶玩法，一篇搞定.md

**新增页面（13个）**：

**概念层** (4个)：
- wiki/concepts/GBrain.md - YC总裁开源的Agent长期记忆系统
- wiki/concepts/长期记忆.md - Agent持久记忆系统，三层架构
- wiki/concepts/多Agent协同.md - 角色隔离+共享上下文+任务委派
- wiki/concepts/横纵分析法.md - 深度研究框架

**工具层** (3个)：
- wiki/tools/GBrain.md - 部署方式与功能详解
- wiki/tools/GStack.md - 编码Skill工作流，7万+Star
- wiki/tools/WorkBuddy.md - 腾讯国产龙虾，微信集成

**人物层** (4个)：
- wiki/people/Garry Tan.md - YC总裁，GStack和GBrain作者
- wiki/people/苍何.md - Hermes Agent深度实践者
- wiki/people/数字生命卡兹克.md - 横纵分析法提出者
- wiki/people/秋芝2046.md - WorkBuddy养成教程作者

**实践层** (3个)：
- wiki/practices/OpenClaw养成路线图.md - 8个阶段完整教程
- wiki/practices/横纵分析法Prompt.md - 完整Prompt模板
- wiki/practices/OpenClaw阿里云部署.md - 阼云官方部署指南

**更新页面** (1个)：
- wiki/tools/Hermes Agent.md - 补充多Agent军团、斜杠命令、迁移指南、文件结构

**页面更新**：
- wiki/index.md（+13条目，总页面数29）
- wiki/log.md（本记录）

---

## [2026-04-22] lint | MiniMax/Kimi 定价信息补充

**操作类型**：数据补充与更新
**执行内容**：
- 用户提供 MiniMax 定价页面链接
- 通过 curl 获取 platform.minimaxi.com 定价页面内容
- 提取 MiniMax-M2.7/M2.5/M2.1 系列详细定价
- 提取 MiniMax Token Plan 套餐详情（¥29-¥899/月）

**MiniMax 定价确认**：

| 模型 | 输入价格 | 输出价格 | 缓存读取 | 缓存写入 |
|-----|---------|---------|---------|---------|
| MiniMax-M2.7 | ¥2.1/百万 | ¥8.4/百万 | ¥0.42/百万 | ¥2.625/百万 |
| MiniMax-M2.7-highspeed | ¥4.2/百万 | ¥16.8/百万 | ¥0.42/百万 | ¥2.625/百万 |
| MiniMax-M2.5/M2.1 | ¥2.1/百万 | ¥8.4/百万 | ¥0.21/百万 | ¥2.625/百万 |

**MiniMax Token Plan 套餐确认**：

|套餐| 月费 | 请求额度 |
|-----|------|---------|
| 基础版 | ¥29/月 | 600次/5小时 |
| 标准版 | ¥49/月 | 1500次/5小时 |
| 高级版 | ¥119/月 | 4500次/5小时 |
| 专业版 | ¥199/月 | 4500次/5小时 |
| 旗舰版 | ¥899/月 | 30000次/5小时 |

**Kimi 定价页面路径确认**：
- pricing/chat-k26（Kimi K2.6）
- pricing/chat-k25（Kimi K2.5）
- pricing/chat-k2（Kimi K2）
- pricing/chat-v1（Moonshot V1）
- 注：具体数值需浏览器访问获取（动态渲染）

**页面更新**：
- wiki/tools/主流模型汇总.md（MiniMax 定价确认、Token Plan 套餐、Kimi 定价路径）

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
| 14 | YC总裁开源GBrain | article | ✓ 本次录入 |
| 15 | Hermes+Kimi Agent军团教程 | article | ✓ 本次录入 |
| 16 | OpenClaw养成路线图 | article | ✓ 本次录入 |
| 17 | 深度研究Prompt横纵分析法 | article | ✓ 本次录入 |
| 18 | WorkBuddy龙虾教程 | article | ✓ 本次录入 |
| 19 | 阼云OpenClaw部署 | article | ✓ 本次录入 |
| 20 | Hermes完整指南 | article | ✓ 本次录入（补充更新） |

**进度**：21/24 完全录入 + 3 已索引 (100%)

---

*日志格式：## [日期] 操作类型 | 标题*
*操作类型：ingest | lint | query | init*