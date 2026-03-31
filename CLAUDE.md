# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
python3 tracker.py
```

No dependencies beyond the Python 3 standard library.

## Architecture

This is a single-file CLI application with two files:

- **`tracker.py`** — all application logic: UI rendering, data access, and menu flow
- **`records.json`** — persistent data store; auto-created on first record save

### Data Format

Records in `records.json` are a flat JSON array:
```json
[{ "date": "YYYY-MM-DD", "content": "...", "timestamp": "YYYY-MM-DD HH:MM:SS" }]
```

### Key Functions

| Function | Purpose |
|---|---|
| `load_records()` / `save_records()` | Read/write `records.json` |
| `add_record()` | Interactive prompt to add today's entry |
| `view_records()` | Display all records grouped by date |
| `show_stats()` | Streak calculation, level system, 7-day heatmap |
| `main()` | Menu loop |

### UI Conventions

- ANSI color constants (`R`, `G`, `Y`, `B`, `M`, `C`, `W`, `DIM`, `BD`, `RST`) are module-level globals
- `play(name)` fires macOS system sounds via `afplay` (silently no-ops on non-macOS)
- `loading_bar()` and `progress_bar()` are purely cosmetic — they don't reflect real progress
## About the Developer

- 开发者是初学者，正在学习Python和Claude Code
- 请用**中文**回复所有问题
- 解释代码时要简单易懂，避免专业术语堆砌
- 修改代码前先说明你打算做什么，等确认再动手
- 每次改动尽量小，改完告诉我改了哪里

## Preferences

- 代码注释请用中文写
- 报错信息请帮我翻译并解释原因
- 不要一次性改太多东西