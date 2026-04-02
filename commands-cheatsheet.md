# 命令速查表

> 常用命令一览，每条包含：命令、说明、示例

---

## 一、终端基础命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `cd 文件夹名` | 进入某个文件夹 | `cd Desktop/learning-tracker` |
| `cd ..` | 返回上一级文件夹 | `cd ..` |
| `ls` | 列出当前文件夹里的所有文件 | `ls` |
| `ls -la` | 列出所有文件（包括隐藏文件），并显示详细信息 | `ls -la` |
| `cat 文件名` | 直接在终端里查看文件内容 | `cat records.json` |
| `code .` | 用 VS Code 打开当前文件夹 | `code .` |
| `code 文件名` | 用 VS Code 打开某个文件 | `code tracker.py` |
| `pwd` | 显示你现在所在的文件夹路径 | `pwd` |

---

## 二、Git 三步存档

> 每次写完代码，执行这三步就能把进度保存到本地仓库。

```bash
# 第一步：把修改的文件加入暂存区
git add .

# 第二步：写一条说明，描述这次改了什么
git commit -m "说明文字"

# 第三步：推送到 GitHub 远程仓库
git push
```

**示例（完整流程）：**
```bash
git add .
git commit -m "完成第9天学习记录"
git push
```

---

## 三、GitHub 相关操作

| 命令 | 说明 | 示例 |
|------|------|------|
| `git init` | 在当前文件夹初始化一个新的 Git 仓库 | `git init` |
| `git clone 地址` | 把 GitHub 上的项目下载到本地 | `git clone https://github.com/你的用户名/项目名.git` |
| `git status` | 查看哪些文件被修改了、哪些还没存档 | `git status` |
| `git log --oneline` | 查看历史存档记录（简洁版） | `git log --oneline` |
| `git pull` | 把 GitHub 上最新的内容同步到本地 | `git pull` |
| `git remote -v` | 查看当前连接的远程仓库地址 | `git remote -v` |

**首次把本地项目推送到 GitHub：**
```bash
git init
git add .
git commit -m "第一次提交"
git remote add origin https://github.com/你的用户名/项目名.git
git push -u origin main
```

---

## 四、Claude Code 启动和退出

| 操作 | 命令/方式 | 说明 |
|------|-----------|------|
| 启动 | `claude` | 在终端里启动 Claude Code |
| 在指定目录启动 | `cd 项目目录 && claude` | 先进入项目再启动，Claude 就能读取项目文件 |
| 退出 | 输入 `/exit` 或按 `Ctrl + C` | 结束当前 Claude Code 会话 |
| 清空对话 | 输入 `/clear` | 清除当前会话内容，重新开始 |
| 查看帮助 | 输入 `/help` | 显示所有可用的命令列表 |

**示例（进入项目并启动）：**
```bash
cd Desktop/learning-tracker
claude
```

---

## 五、快速记忆口诀

```
终端导航：cd 进，ls 看，cat 读，code 开编辑器
Git存档：add 装箱，commit 贴标签，push 寄出去
GitHub同步：clone 下载，pull 更新，push 上传
Claude Code：claude 启动，/exit 退出
```
