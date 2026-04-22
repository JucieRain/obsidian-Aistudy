---
title: "使用git实现obsidian同步"
source: "https://zhuanlan.zhihu.com/p/1895499940731543837"
author:
  - "[[Leung好响就是好头]]"
published:
created: 2026-04-12
description: "Obsidian是一款优秀的知识网络软件，用来记笔记和草图十分方便，但美中不足的是同步功能需要付费，所幸Obsidian的git第三方工具可以实现github同步。下面是教程： 一、前提确保配置以下工具： 1. git：Git - Downl…"
tags:
  - "clippings"
---
Obsidian是一款优秀的知识网络软件，用来记笔记和草图十分方便，但美中不足的是同步功能需要付费，所幸Obsidian的git第三方工具可以实现 [github](https://zhida.zhihu.com/search?content_id=256438446&content_type=Article&match_order=1&q=github&zhida_source=entity) 同步。下面是教程：

### 一、前提确保配置以下工具：

  
1\. git：

2\. Obsidian:

[![](https://picx.zhimg.com/v2-7e7d711390083e54b19a5aacb0e1042d_180x120.jpg)](https://link.zhihu.com/?target=https%3A//obsidian.md/)

3\. 你的github账户

### 二、创建私有github仓库

1. 在个人的github账户的repositories菜单栏中选择NEW，创建一个私有仓库，比如仓库名称设置为test，注意勾选private选项：
![](https://pic1.zhimg.com/v2-7cda23769aa459345a98d90398c8289c_1440w.jpg)

初始化私有仓库

2\. ok，现在你已经有了一个远程存储仓库了，由于这个仓库是私有的（因为它主要存储你的私人笔记），所以我们选择更为隐私的 [SSH](https://zhida.zhihu.com/search?content_id=256438446&content_type=Article&match_order=1&q=SSH&zhida_source=entity) 的登录方式，这样可以通过本地存储的 [私钥](https://zhida.zhihu.com/search?content_id=256438446&content_type=Article&match_order=1&q=%E7%A7%81%E9%92%A5&zhida_source=entity) 和github服务器上的 [公钥](https://zhida.zhihu.com/search?content_id=256438446&content_type=Article&match_order=1&q=%E5%85%AC%E9%92%A5&zhida_source=entity) 自动验证身份。下面是在github上配置SSH的方式：

首先使用本地安装的git工具设置一个ssh本地私钥，这会在你本地的.ssh目录下创建私钥文件：

```
ls ~/.ssh/id_ed25519.pub || ls ~/.ssh/id_rsa.pub

# 如果没有相应文件，使用你的一个邮箱创建一个即可
ssh-keygen -t ed25519 -C "your_email@example.com"
```

然后找到对应的私钥文件复制其内容，一般在你的用户目录下的.ssh文件中。

![](https://pic4.zhimg.com/v2-1bdd337e64d337f9359f71e96daaf14f_1440w.jpg)

之后在服务器端（github个人账户）中配置公钥。登录 GitHub，点击右上角头像 → **Settings** → **SSH and GPG keys** 。选择new ssh key，如图，我创建了一个名为obsidian的公钥

![](https://pic1.zhimg.com/v2-dbe205d37d377f98dc861e359e540b5a_1440w.jpg)

ok，创建完私钥和公钥以后，可以测试一下是否该配置存在：

```
# 测试ssh配置
ssh -T git@github.com
```

如果配置成功，会提示如下成功信息：

```
Hi your_name! You've successfully authenticated, but GitHub does not provide shell access.
```

### 三、将远程仓库克隆到本地

1. 因为github不是公有云，所以推荐采用clone的方式，将远程仓库克隆到本地，确保obsidian的git配置和远程完全一致。切记不要使用自己的原有本地文件夹进行 [git init](https://zhida.zhihu.com/search?content_id=256438446&content_type=Article&match_order=1&q=git+init&zhida_source=entity) 和 push 远程操作，否则会出现上述git不匹配的问题！
```
# 打开终端，进入目标目录（如 Documents）：
cd ~/Documents
# 克隆仓库（替换为你的仓库地址）：
git clone git@github.com:yourusername/your-repo.git
# 如果提示 Permission denied，确认 SSH 密钥已正确加载。
```

如果你想把原有的笔记（比如之前的一个本地文件夹）也同步到这个克隆仓库，很简单，只需要把你的原有文件夹copy一份到克隆下来的仓库然后使用git同步即可。

2\. 由于我们还没有在仓库中创建分支，只是初始化了密钥，所以还需要在本地做一个分支，然后推送到远程，这样能够确保git是完备的，可以被obsidian正确识别。继续使用git bash:

```
# 创建一个分支
echo "# My Notes" >> README.md
git add README.md
git commit -m "Initial commit"

# 推送内容到远程，验证git完备性，这里我推送到了主分支
git push -u origin main

# push之后再拉取回本地，确保本地也有main分支：
git fetch origin

# 当然如果本地没有main也可以强制关联：
git branch -u origin/main main

# 最后展示一下分支：
git remote show origin
```

ok，配置好后应该有如下信息：  

![](https://pic4.zhimg.com/v2-d341912f1b4b20f36922188f82e7a583_1440w.jpg)

### 四、Obsidian配置git第三方工具并打开本地的克隆项目

现在完事具备了，我们要打开obsidian，安装第三方的git插件：

具体步骤是打开设置->解除安全模式->选择第三方插件->选择插件市场，如图：  

![](https://pic4.zhimg.com/v2-5b77242e00867f2e67721cf72853a05f_1440w.jpg)

然后搜索git安装：  

![](https://pica.zhimg.com/v2-e2806821ffb2c63c900349547b26bcc2_1440w.jpg)

ok，安装好以后在插件设置里面配置一下同步间隔和git执行文件路径，git执行文件路径可以使用 `where git` 查看：  

![](https://pic2.zhimg.com/v2-53505978a83af11c8f0a9fec6a2ba95b_1440w.jpg)

![](https://pic1.zhimg.com/v2-d2bba39ecf31d5b5a3e813869442ba70_1440w.jpg)

ok，再测试一下是否能够完成同步：  
在主界面中随便写一个笔记：  

![](https://pic2.zhimg.com/v2-a8b8472aac5a93d34789f4d6b3be01f7_1440w.jpg)

可以看到git已经正确识别到了更改，同步一下试试，点击提交同步按钮：  

![](https://pic2.zhimg.com/v2-601dc783c2f623dda5756a13ae9c89b9_1440w.jpg)

如果输出pushed xx信息，说明配置成功。

![](https://pic2.zhimg.com/v2-918b8f0e6d52117f3b2b928377d887f5_1440w.jpg)

### 五、总结

以上就是obsidian使用git工具同步的全部内容了，相信你一定有所收获！

编辑于 2025-04-15 16:49・北京[Git](https://www.zhihu.com/topic/19557710)[Obsidian](https://www.zhihu.com/topic/21349840)[同步- remotely save- obsidian git](https://www.zhihu.com/topic/26483364)