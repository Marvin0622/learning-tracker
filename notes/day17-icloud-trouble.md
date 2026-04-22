# Day 17 故障排查笔记：iCloud 把 Git 仓库搞坏了

## 现象
- `cd ~/Desktop/learning-tracker` 报错：no such file or directory
- 用 find 找到项目跑到了 iCloud 里
- 进去后 articles 文件夹里的文章全没了
- `git pull` 报错：not a git repository

## 根本原因
macOS 桌面默认同步到 iCloud。iCloud 的"优化存储"会把
本地文件卸载到云端，包括 .git 文件夹里的关键文件
（HEAD、config、index），导致 Git 仓库失效。

## 解决方案
1. 用 `find ~ -name "xxx" -type d` 找文件夹位置
2. 项目坏了不要硬修，直接 `git clone` 重新下载
3. 把项目放在 `~/` 下，不要放桌面（避开 iCloud）

## 今天学的新命令
- `find ~ -name "xxx" -type d`：搜文件夹
- `git pull`：从 GitHub 拉取更新
- `git clone <地址>`：从 GitHub 完整下载项目

## 教训
桌面 ≠ 安全位置。代码项目要放在不被云盘同步的地方。