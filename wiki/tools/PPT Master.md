---
title: PPT Master
created: 2026-07-05
updated: 2026-07-05
sources: ["[[Clippings/articles/PPT Master：开源AI PPT生成工具.md]]", "[[Clippings/articles/13个开源PPT Skill合集.md]]"]
tags: [工具, PPT, 开源, python, AI工具]
status: stable
---

# PPT Master

> 开源 AI PPT 生成工具（GitHub 2.26万 Star），生成真正的原生可编辑 .pptx，每个元素都能在 PowerPoint 中逐一修改

## 官方资源

| 资源 | 链接 |
|------|------|
| GitHub | https://github.com/hugohe3/ppt-master |
| 中文文档 | https://github.com/hugohe3/ppt-master/blob/main/README_CN.md |
| 官网 | https://hugohe3.github.io/ppt-master/ |

## 核心定位

与图片式 AI PPT（生成即定型，改不了）不同，PPT Master 采用 **SVG 作为中间格式**，精确转换为 PowerPoint 原生 DrawingML 形状、文本框、图表。每个元素都可独立编辑。

## 三阶段驾驶框架

| 阶段 | 角色 | 职责 |
|------|------|------|
| 1 | **Strategist 策略师** | 内容分析，确认八项设计规范（画布/页数/受众/风格/配色/图标/排版/图片） |
| 2 | **Executor 执行师** | 逐页生成 SVG 视觉内容，8条纪律规则强制运行，质量门零错误放行 |
| 3 | **后处理引擎** | SVG→DrawingML 精确转换，Office 兼容模式（新版可编辑 + 旧版 PNG 兜底） |

## 关键特性

- 72 种图文版式技法（Primary + Modifier 自由组合）
- 三种执行师模式：General / Consultant / Consultant_Top（MBB 顶级咨询级）
- 10+ 画布格式：16:9、小红书 3:4、抖音 9:16、A4 印刷等
- 支持参考自有模板，提取品牌色和母版保持调性
- 多 AI 模型兼容：Claude、GPT、Gemini、Kimi、GLM
- 完全本地运行，数据安全

## 与 PPT Director 的对比

| 维度 | PPT Master | PPT Director |
|------|------------|--------------|
| 平台 | 独立工具（Python） | Claude Code Skill |
| 输出 | 原生 .pptx（SVG→DrawingML） | 原生 .pptx（python-pptx） |
| 受众蒸馏 | 无 | 有（依赖女娲） |
| 编辑性 | 逐元素可编辑 | 可编辑 |
| 价格 | MIT 开源免费 | 免费 |
| 特色 | 72种版式、多风格、自有模板 | 认知蒸馏、三重评审、受众卡 |

> — [[Clippings/articles/PPT Master：开源AI PPT生成工具.md]]

## 安装

```bash
git clone https://github.com/hugohe3/ppt-master.git
cd ppt-master
pip install -r requirements.txt
```

前置条件：Python 3.10+

## PPT Skill 生态速览 | 2026-07-05

> — [[Clippings/articles/13个开源PPT Skill合集.md]]

除 PPT Master 外，开源社区还有 12 个 PPT 相关 Skill，按交付类型分为四类：

| 类型 | 代表项目 | 特点 |
|------|---------|------|
| **原生可编辑 PPTX** | pptx-from-layouts-skill, Huashu Design, Fergana-Labs | 符合企业模板、Agent 视觉生成、Node.js 操作 |
| **HTML 演示** | Frontend Slides (2.3万★), Guizang PPT, HTML PPT Skill | 视觉上限高、单文件横向翻页、演讲者模式 |
| **图片式卡片** | Baoyu Slide Deck, gpt-image2-ppt-skills | 文章快速转卡片、仿模板版式 |
| **平台与框架** | Presenton, PPTAgent, Anything to NotebookLM | 本地部署、Agentic 框架、多格式输出 |

选择原则：先想清楚要交付什么——可编辑文件、现场演讲、还是图片卡片——再选工具。

> — [[Clippings/articles/13个开源PPT Skill合集.md]]

## 参见

- [[tools/PPT Director Skill]] — Claude Code 内 PPT 工作流
- [[tools/Claude Code]]
