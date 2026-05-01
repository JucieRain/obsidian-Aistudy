---
title: Hermes Agent五大配置模块
created: 2026-04-30
updated: 2026-04-30
sources:
  - "[[Clippings/articles/装完 Hermes 一定要配置这五套系统，秒变满配版，能力提升数倍不止]]"
tags:
  - Hermes Agent
  - Agent配置
  - 记忆系统
status: stable
---

# Hermes Agent五大配置模块

> 装完 Hermes 只是起点，配置才是拉开差距的关键。裸装和满配完全是两种工具。

## 五大配置模块

| 模块 | 内容 | 效果 |
|-----|------|------|
| 身份与记忆 | SOUL.md、Hindsight | 让它知道你是谁，记住你说过的 |
| 感知能力 | 内容抓取工具 | 让它读懂全网信息 |
| 表达能力 | 语音+图片生成 | 让它能说能画 |
| 效率与成本 | Token管控工具 | 精细控制成本 |
| 生态导航 | 资源入口 | 一站式获取资源 |

## 模块一：身份与记忆

### SOUL.md 定义人格

使用 agency-agents-zh 库（211个中文角色模板）：
- GitHub: https://github.com/jnMetaCode/agency-agents-zh
- 包含46个中国市场原创智能体（小红书、抖音、飞书、钉钉等）
- 按部门分类（工程、设计、营销、产品等18个）

### Hindsight 记忆系统替换

```bash
hermes memory setup
# 选择 hindsight
```

对比内置 MEMORY：

| 维度 | 内置 MEMORY | Hindsight |
|-----|-------------|-----------|
| 写入机制 | Hermes认为重要才写 | 自动提取实体/事实/关系 |
| 容量上限 | ≈2200字符 | 无上限 |
| 知识组织 | 线性文本 | 知识图谱 |

Hindsight API Key：https://ui.hindsight.vectorize.io/connect

验证：
```bash
hermes memory status
```

## 模块二：感知能力（内容抓取）

| 工具          | 用途     |
| ----------- | ------ |
| Jina Reader | 单页抓取   |
| Crawl4 AI   | 批量深度抓取 |
| Scrapling   | 反爬绕过   |
| CamoFox     | 隐身浏览器  |

CamoFox 和 Scrapling 是官方原生/可选技能，直接通过 `hermes tools + pip` 启用。

## 模块三：搜索与文档处理

| 工具 | 用途 |
|-----|------|
| Tavily | AI专用搜索，1000次/月免费 |
| DuckDuckGo | 零成本兜底搜索 |
| Pandoc | 万能格式转换器 |
| Marker | PDF转Markdown增强 |

## 模块四：表达能力

| 工具 | 用途 |
|-----|------|
| Whisper | 语音识别，99+语言 |
| Edge TTS | 语音合成，免费使用 |
| Fal.ai | 图片生成 |
| FLUX Skill | 高质量出图 |

## 模块五：效率与成本

### Tokscale Token监控

```bash
# npm
npx tokscale@latest

# Bun
bunx tokscale@latest
```

命令：
```bash
tokscale                  # 全局总览
tokscale --hermes         # 只看 Hermes
tokscale --hermes --week  # 过去7天趋势
tokscale models           # 按模型统计
```

### RTK Token压缩

Rust写的零依赖CLI代理，智能压缩终端输出，减少60-90% Token：

```bash
# Homebrew
brew install rtk

# 一键脚本
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh

# 集成到 Hermes
rtk init -g
```

### Hermes-agent-self-evolution

遗传算法自动优化Agent提示词和行为：

```bash
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
pip install -e ".[dev]"
```

## 生态入口

| 资源 | 地址 |
|-----|------|
| awesome-hermes-agent | 一站式资源汇总 |
| hermes-ecosystem | 80+工具可视化地图 |

## 相关页面

- [[Hermes Agent]] - 基础使用教程
- [[MemOS]] - 另一种记忆插件选择
- [[长期记忆]] - 记忆系统概念

## 来源

- [[Clippings/articles/装完 Hermes 一定要配置这五套系统，秒变满配版，能力提升数倍不止]] - 科技君，2026-04-23