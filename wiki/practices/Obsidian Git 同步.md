---
title: Obsidian Git 同步
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[Clippings/articles/使用git实现obsidian同步.md]]"
tags: [实践, Obsidian, Git, 同步]
status: stable
---

# Obsidian Git 同步

> 使用 Git 实现 Obsidian 跨设备同步，替代付费同步

## 为什么用 Git 同步

- Obsidian 官方同步需付费
- Git 同步免费、可控
- 支持版本历史
- 跨平台通用

## 配置流程

### 1. 创建私有仓库

GitHub → New repository → 勾选 Private

### 2. 配置 SSH 密钥

```bash
# 检查是否有密钥
ls ~/.ssh/id_ed25519.pub || ls ~/.ssh/id_rsa.pub

# 如无则创建
ssh-keygen -t ed25519 -C "your_email@example.com"

# 测试连接
ssh -T git@github.com
```

### 3. 克隆仓库

```bash
cd ~/Documents
git clone git@github.com:yourusername/your-repo.git
```

### 4. 安装 Obsidian Git 插件

设置 → 关闭安全模式 → 第三方插件 → 搜索 Git

### 5. 配置插件

- 设置同步间隔
- 配置 Git 执行文件路径（`where git` 查看）

## 最佳实践

- **不要**用现有文件夹 `git init` 再 push
- **推荐**先 clone 再把原有笔记复制进去
- 定期检查同步状态

## 参见

- [[tools/Obsidian]]

## 来源

- [[Clippings/articles/使用git实现obsidian同步.md]]