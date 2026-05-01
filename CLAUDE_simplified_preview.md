# LLM Wiki 知识库维护规则（精简版）

> 基于 Karpathy 的 LLM Wiki 方法，为 AI 落地实践研究构建的第二大脑系统

---

## 一、系统架构

三层架构：素材层(Clippings/) → 知识层(wiki/) → 日志层(Journal/)

```
AIstudy/
├── Clippings/           # 📥 素材入口（只读）
│   ├── articles/        # 网页剪藏
│   ├── videos/          # 视频素材
│   ├── papers/          # PDF 论文
│   └── others/          # 其他
├── wiki/                # 🧠 AI 维护的知识库
│   ├── index.md         # 总索引
│   ├── log.md           # 操作日志
│   ├── concepts/        # 概念页
│   ├── tools/           # 工具页
│   ├── people/          # 人物页
│   ├── practices/       # 实践指南
│   └── synthesis/       # 综合分析
├── Journal/             # 📝 个人日记（人写，AI读）
└── archive/             # 已处理素材归档
```

---

## 二、素材分类规则

### 分类标准

| 类型 | 判断标准 | 目标目录 |
|-----|---------|---------|
| article | `.md` + `source: http` frontmatter | `Clippings/articles/` |
| video | 提及 YouTube/B站/抖音 或文件名含「视频」「教程」 | `Clippings/videos/` |
| paper | `.pdf` 学术论文/白皮书 | `Clippings/papers/` |
| thought | 来自 `Journal/` 的个人创作 | 作为素材引用，不移动 |

### 分类判断步骤

1. **PDF 文件** → 直接归类为 paper
2. **Markdown 文件**：
   - 读取 frontmatter，检查是否有 `source` 字段且以 `http` 开头 → article
   - 检查文件名是否含关键词：视频、教程、演示、直播、YouTube、B站、抖音 → video
   - 检查内容是否包含 `youtube.com` 或 `bilibili.com` → video
   - 默认 → article
3. **其他文件** → others

### 处理优先级

1. articles/ → 最高（更新频率高）
2. videos/ → 次优先
3. papers/ → 批量处理
4. Journal/ 最新 → 定期整合

---

## 三、核心操作

### 3.1 Ingest（录入）

**触发**：扫描新素材 / 用户请求「录入最新」

**步骤**：
1. 扫描 Clippings/ 根目录，识别未分类素材
2. 按分类规则判断类型，移动到对应子目录
3. 读取素材，提取：核心概念、工具/产品、人物、关键论点
4. 创建/更新 wiki 页面
5. 更新 index.md 和 log.md

### 3.2 Query（查询）

1. 读取 index.md 定位相关页面
2. 深入阅读相关 wiki 页面
3. 如需补充，读取原始素材（archive/）
4. 综合回答，引用来源

### 3.3 Lint（健康检查）

**检查项目**：

| 检查项 | 说明 | 严重程度 | 修复方式 |
|-------|------|---------|---------|
| 孤儿页面 | 无入链的 wiki 页面 | 🟡 中 | 添加到相关页面或 index.md |
| 缺失页面 | 多次提及但无独立页面 | 🟡 中 | 创建新页面 |
| 断链 | wikilink 指向不存在页面 | 🔴 高 | 创建页面或修复链接 |
| 矛盾检测 | 同一事实说法不同 | 🔴 高 | 标注矛盾，建议统一 |
| 过时检测 | 素材更新但 wiki 未同步 | 🟡 中 | 标注待更新 |
| 漂移检测 | wiki 内容与原文不一致 | 🔴 高 | 对照原文修复 |

**周期**：常规每周 / 深度每月（随机抽 5 页对比原文）

**输出**：生成 `wiki/lint-report-[日期].md`，等待用户确认后执行修复

---

## 四、溯源机制（防漂移）

### 核心规则

**关键事实必须标注来源行号**：

```markdown
# 正确示例
该公司营收"10.3 亿元"。
> — Clippings/articles/原文.md, L42-45
```

### 必须标注的内容

| 类型 | 示例 |
|-----|------|
| 数字/百分比 | "47.2%" → 标注行号 |
| 具体结论 | "该公司是行业第一" → 标注行号 |
| 人物观点 | "Karpathy认为..." → 标注行号 |
| 时间/日期 | "2026年4月发布" → 标注行号 |

### 可不标注

- AI 自己总结的框架、分类
- 不依赖素材的常识
- 推导结论（推导依据需标注）

---

## 五、页面格式规范

### wiki 页面通用格式

```markdown
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [来源素材列表，使用 wikilink 格式]
tags: [标签列表]
status: draft | stable | needs-update
---

# 页面标题

> 一句话定义/摘要

## 核心内容

[主要内容，使用段落+列表形式]

## 相关概念

- [[概念A]]
- [[概念B]]

## 参见

- [[相关工具]]
- [[相关人物]]

## 来源

- [[Clippings/articles/原文1]]
- [[Clippings/videos/视频笔记]]
```

**Frontmatter 字段说明**：

| 字段 | 必填 | 说明 |
|-----|-----|------|
| title | ✓ | 页面标题 |
| created | ✓ | 创建日期 |
| updated | ✓ | 最后更新日期 |
| sources | ✓ | 来源素材列表（wikilink 格式） |
| tags | ✓ | 标签列表 |
| status | ✓ | 状态：draft/stable/needs-update |

### index.md 格式

按类别组织表格：概念、工具、人物、趋势、实践、综合

每类表格包含：页面（wikilink） | 摘要 | 来源数

首行注明：最后更新日期 | 总页面数

### log.md 格式

每条记录包含：
- 日期 + 操作类型（ingest/lint）
- 素材路径
- 新增页面列表
- 更新页面列表

---

## 六、定时任务

| 任务 | 周期 |
|-----|------|
| 素材扫描 | 每次会话 |
| 常规体检 | 每周 |
| 深度体检 | 每月 |
| Journal 整合 | 每周 |

调度记录：`wiki/schedule.jsonl` 记录上次执行时间和下次到期

---

## 七、特殊规则

### 优先级

- 高：Karpathy、OpenAI、Anthropic 相关
- 中：工具教程、实践案例
- 低：一般新闻、观点

### 链接规范

- 内部：`[[页面名]]` 或 `[[路径/页面名]]`
- 来源：`[[Clippings/articles/原文]]`

### 🔴 禁止操作

- ❌ 不可修改 `Journal/` 内容
- ❌ 不可删除 `Clippings/` 原始素材（只能移动到 archive）
- ❌ 不可在没有用户确认时执行修复

---

*本规则持续迭代优化*