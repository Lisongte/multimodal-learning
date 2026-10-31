# 多模态学习与 VLM 实验

学习周期：2026-11-02 至 2027-01-24，每周约 20 小时。
目标：掌握训练、调试和评测基础，完成一个可复现的视觉语言模型项目，为 2027 年 3 月实习申请做准备。

## 目录

- `exercises/`：基础练习，按周组织。
- `notes/`：概念、论文、调试笔记。
- `src/`：后期 VLM 主项目代码。
- `progress/`：每日真实进度、证据和下一步。
- `scripts/`：每日记录和手动同步工具。
- `ROADMAP.md`：12 周目标与验收标准。

大数据和模型可放本机或移动硬盘；根目录 `data/`、`models/`、`checkpoints/` 已忽略。
不要将公司的数据、内部代码、访问令牌或个人敏感信息放入仓库。

## 每天的流程

```bash
cd /Users/jimmylee/project
python3 scripts/progress.py
```

打开脚本打印的文件，填写当天实际完成的内容。学习完成后先检查改动，再提交并推送：

```bash
git status
git diff
bash scripts/sync.sh "学习：张量与自动求导"
```

同步脚本只添加学习目录及仓库说明文件；提交后推送到 origin 的当前分支。
仅修改文件不会自动上传。若网络或认证失败，已完成的本地提交会保留，可修复后再次执行。
脚本默认不会添加新建在根目录的其他文件，需要时用 `git add 路径` 明确加入。

## 先学会这几个 Git 命令

```bash
git status                       # 查看修改和暂存状态
git diff                         # 查看尚未暂存的修改
git add exercises/ progress/      # 选择本次要记录的文件
git diff --cached                # 查看即将提交的内容
git commit -m "学习：完成线性回归"  # 保存本地版本
git push                         # 上传已提交版本
git log --oneline -5              # 查看最近 5 次提交
git pull --ff-only                # 开始在另一台电脑继续前，获取远端更新
```

`commit` 保存本地历史，`push` 上传 GitHub。个人学习前期使用 main 分支即可。
不要在尚未理解时使用 `reset --hard`、`clean -fd` 或强制推送。

## GitHub 仓库

https://github.com/Lisongte/multimodal-learning

本地使用 main 分支，origin 已设置为：

```text
https://github.com/Lisongte/multimodal-learning.git
```

本机首次登录（运行后根据提示在网页输入一次性验证码）：

```bash
bash scripts/github-login.sh
```

该脚本使用项目本地官方 GitHub CLI，只修改本仓库的 Git 凭据配置。不要发送验证码之外的令牌或密码到聊天中。

首次推送命令（成功后日常可用同步脚本）：

```bash
git push -u origin main
```

HTTPS 推送需要受支持的身份验证方式（例如 Git Credential Manager、GitHub CLI 或 PAT）；GitHub 账户密码不能直接用于 Git 推送。
不要把访问令牌写进远端 URL、代码或聊天记录。项目本地 CLI 配置位于已忽略的 `.local/` 目录，不应上传。

## 学习与 AI coding

基础训练循环、Attention 等先自己尝试；AI 辅助后，要能解释输入、输出和关键操作。
实验记录保留配置、数据划分、实际结果和失败案例。尚未执行的学习或实验不标记完成。
