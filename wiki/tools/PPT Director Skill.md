---
title: PPT Director Skill
created: 2026-07-05
updated: 2026-07-05
sources: ["[[Clippings/articles/AI驱动的PPT工作流：女娲Skill+PPT Director.md]]"]
tags: [工具, Skill, Claude Code, PPT, AI工作流]
status: stable
---

# PPT Director Skill

> Claude Code PPT 导演工具：根据材料、受众、评审标准，自动调度从大纲到 .pptx 的全流程

## 安装

```bash
npx skills add hermess/ppt-director
```

依赖：`pip install python-pptx`

## 核心设计

不生成故事绘本式 PPT，而是生成**可编辑、能修改、真正能拿去汇报的 PPT**。

## 五阶段自动调度

Director 会根据你当前拥有的材料自动判断从哪个阶段开始：

| 阶段 | 判断依据 | 产出 |
|------|----------|------|
| **A 灵感激发** | 只有一个主题/想法 | 思路发散、受众确认、初步规划 |
| **B 内容打磨** | 有思路或原始材料 | 观点型大纲、标准交付文档 |
| **C 视觉定义** | 已有标准交付文档 | 页型分配、风格映射 |
| **D 代码生成** | 视觉定义已完成 | python-pptx 代码 → .pptx 文件 |
| **E 迭代优化** | 已有 PPT 初稿 | 三重评审 → 修改清单 |

## 核心机制

### 内容规划公式

`受众关注什么（audience-card） × 专家会怎么审（reviewer-card） × 你有什么素材 = 每页放什么`

### 17 种标准页型

| 编号 | 名称 | 适用场景 |
|------|------|----------|
| T01 | 封面页 | 标题+副标题+汇报人 |
| T04 | 纯文字观点页 | 一核心观点+3 个要点 |
| T05 | 数据图表页 | 柱状/折线/饼图 |
| T06 | 对比页 | 改革前 vs 改革后 |
| T10 | 数字突出页 | 1-3 个大数字+说明 |
| T17 | 总结页 | 结论+下一步 |

### 默认风格卡（蓝色汇报）

- 色彩：深蓝 #003366、科技蓝 #0066CC、活力橙 #FF6600、浅灰 #F5F7FA
- 版式：标题区 1/5、内容区 3/5、数据可视化优先
- 禁忌：无圆角大装饰、禁用卡通图标、每页文字 ≤50 字

## 三重评审关卡（E 阶段）

1. **受众视角评审**（基于 audience-card）：改善建议，改不改酌情
2. **专家视角评审**（基于 reviewer-card）：必须改的硬伤
3. **表达优化评审**（基于 best-practices）：改了更专业

## 使用示例

```markdown
情况1：只有一个想法
我要做一个PPT，主题是"XX区数字化改革成效汇报"，受众是省级领导
帮我用PPT Director来规划

情况2：有材料了
我有以下材料，需要做成PPT：[粘贴材料]
受众：XX领导，目的：说服对方做XX决策，时长：X分钟
用PPT Director帮我从B阶段开始

情况3：已经有PPT初稿
我已经有一份PPT：[文件或内容]
帮我用PPT Director做一次三重评审
```

## 在完整工作流中的位置

```
女娲（蒸馏受众+评审）
    ↓ audience-card + reviewer-card
PPT Director（调度生产：大纲→交付文档→页型→代码→.pptx）
    ↓
达尔文（可选打磨优化）
```

> — [[Clippings/articles/AI驱动的PPT工作流：女娲Skill+PPT Director.md]]

## 参见

- [[tools/女娲Skill]]
- [[concepts/认知蒸馏]]
- [[tools/Claude Code]]
