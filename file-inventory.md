# 项目文件清单报告

> 生成时间：2026-04-04
> 项目目录：`Desktop/learning-tracker`

---

## 文件总览

| 文件名 | 大小 | 最后修改时间 | 用途说明 |
|--------|------|-------------|---------|
| `tracker.py` | 15.1 KB | 2026-03-30 19:29 | 核心应用程序。一个命令行学习进度追踪器，功能包括：添加每日学习记录、查看历史记录、计算连续打卡天数、显示等级系统和7天热力图，带 ANSI 彩色界面和 macOS 系统音效。 |
| `records.json` | 283 B | 2026-03-30 19:35 | 数据存储文件。以 JSON 数组格式保存所有学习记录，每条记录包含日期、学习内容和录入时间戳。目前存有2条记录。 |
| `CLAUDE.md` | 1.7 KB | 2026-03-31 10:54 | Claude Code 项目配置文件。说明项目架构、运行方式和关键函数，同时记录了开发者偏好（初学者、用中文回复、改动前先说明）。 |
| `commands-cheatsheet.md` | 2.8 KB | 2026-04-02 17:21 | 命令速查手册。整理了终端基础命令、Git 三步存档流程、GitHub 操作、Claude Code 启动退出方法，以及方便记忆的口诀，供学习过程中随时查阅。 |
| `content-ideas.md` | 2.7 KB | 2026-04-01 09:10 | 公众号选题策划文档。围绕"AI + 教育"主题，面向高中生家长和教师，规划了10个选题，每条附有简介和建议发布时机。 |
| `article-draft-01.md` | 4.5 KB | 2026-04-01 09:33 | 文章草稿（Markdown 版）。`content-ideas.md` 中某个选题的正文初稿，Markdown 格式便于编辑和修改。 |
| `article-draft-01.html` | 17.8 KB | 2026-04-01 09:36 | 文章草稿（HTML 版）。与上方同一篇文章的 HTML 渲染版本，可直接在浏览器预览排版效果，文件较大是因为包含了完整的 HTML 结构和样式。 |
| `instructions/teaching-method.md` | 1.9 KB | 2026-03-31 10:54 | 教学方法说明文档。记录了45天学习计划的教学原则（新概念先解释、五位一体教学法、艾宾浩斯复习曲线），以及已总结的有效做法和需避免的问题。 |

---

## 目录结构

```
learning-tracker/
├── tracker.py                    # 主程序
├── records.json                  # 学习记录数据
├── CLAUDE.md                     # Claude Code 配置
├── commands-cheatsheet.md        # 命令速查表
├── content-ideas.md              # 公众号选题策划
├── article-draft-01.md           # 文章草稿（Markdown）
├── article-draft-01.html         # 文章草稿（HTML）
└── instructions/
    └── teaching-method.md        # 教学方法说明
```

---

## 文件分类

### 应用程序（2个文件）
- `tracker.py`：主程序逻辑
- `records.json`：持久化数据

### 学习参考资料（2个文件）
- `commands-cheatsheet.md`：命令速查
- `instructions/teaching-method.md`：教学规范

### 内容创作素材（3个文件）
- `content-ideas.md`：选题库
- `article-draft-01.md`：文章草稿
- `article-draft-01.html`：文章预览版

### 项目配置（1个文件）
- `CLAUDE.md`：Claude Code 项目说明

---

## 备注

- 项目已初始化 Git 仓库（`.git/` 目录存在）
- 全部文件均为纯文本格式，无需额外依赖即可查看
- `article-draft-01.html`（17.8 KB）是当前体积最大的文件，因包含完整 HTML 结构
