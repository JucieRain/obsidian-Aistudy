---
title: "PPT Master：开源AI PPT生成工具"
source: https://mp.weixin.qq.com/s/Wtgn3G6et93_sX8ql-3eHA
date: 2026-07-05
fetched: 2026-07-05
tags: ["PPT", "开源", "AI工具", "SVG", "python"]
referenced_by: ["[[wiki/tools/PPT Master]]"]
---

# PPT Master：开源AI PPT生成工具

> 原文链接：https://mp.weixin.qq.com/s/Wtgn3G6et93_sX8ql-3eHA
> GitHub: https://github.com/hugohe3/ppt-master (2.26万 Star)
> 作者：何雨果（Hugo He）

## 核心定位

真正的原生可编辑PPTX，每个元素都能在PowerPoint里逐一点击修改，而非图片拼凑或HTML演示。

## 六大核心功能

1. 任意文档一键生成：支持 PDF、DOCX、图片、HTML、EPUB、LaTeX、微信文章链接
2. 多风格+原生动画+音频旁白：内置杂志风、财经数据风、瑞士风、孟菲斯等；支持 PowerPoint 原生转场和入场动画
3. 参考自有模板：上传公司品牌PPT模板，提取主题色、字体、母版/版式
4. AI生图+网络图库双引擎：支持 gpt-image-2、DALL·E、Gemini、FLUX等；Pexels/Pixabay/Openverse
5. 出版物级图表+72种版式：SVG渲染图表转为原生PPT形状，三种执行师模式（General/Consultant/Consultant_Top即MBB顶级咨询级）
6. 10+种画布格式：16:9、4:3、小红书3:4、朋友圈1:1、抖音9:16、A4印刷等

## 架构：三阶段驾驶框架

1. Strategist 策略师 — 内容分析，确认八项设计规范（画布/页数/受众/风格/配色/图标/排版/图片）
2. Executor 执行师 — 逐页生成 SVG 视觉内容，8条纪律规则强制运行
3. 后处理引擎 — SVG→DrawingML 精确转换，Office 兼容模式

核心设计哲学："AI 放大的是你已有的能力——你有设计感和内容判断力，它帮你快速落地。"

## 对比其他 AI PPT 工具

| 维度 | PPT Master | 图片式AI PPT | Gamma |
|------|------------|--------------|-------|
| 输出格式 | 原生 .pptx | 一张大图 | HTML网页 |
| 文本可修改 | 每个文本框独立 | 改不了 | 改不了 |
| 颜色/形状可调 | 逐形状调色 | 不可调 | 不可调 |
| 动画效果 | 原生 PowerPoint 动画 | 假动画 | 假动画 |
| 数据安全 | 全流程本地 | 云端 | 上传云端 |
| 价格 | 免费开源 + API 按量 | 各家定价 | $8-20/月 |

## 多环境覆盖

运行环境：VS Code、Cursor、Claude Code CLI、Codex CLI 等
AI模型：Claude Opus/Sonnet（推荐）、GPT-5.5+、Gemini、Kimi、GLM
推荐组合：Claude 大上下文窗口 + gpt-image-2 生图

## 快速上手

```bash
git clone https://github.com/hugohe3/ppt-master.git
cd ppt-master
pip install -r requirements.txt
```

前置条件：Python 3.10+，其余依赖自动安装。输出到 exports/ 目录。

## 价格

MIT 协议开源免费，仅需 AI 模型 API 用量费用。
