#!/usr/bin/env python3
# tracker.py - 炫酷学习进度追踪器

import json
import os
import sys
import time
import datetime
import subprocess
from pathlib import Path

RECORDS_FILE = 'records.json'

# ── ANSI 颜色 ──────────────────────────────────────────────────────────────────
R  = '\033[91m'; G  = '\033[92m'; Y  = '\033[93m'; B  = '\033[94m'
M  = '\033[95m'; C  = '\033[96m'; W  = '\033[97m'; DIM = '\033[2m'
BD = '\033[1m';  RST = '\033[0m'

PALETTE = [C, B, M, C, B, M]

# ── 音效 ───────────────────────────────────────────────────────────────────────
_SOUNDS = {
    'start':     '/System/Library/Sounds/Blow.aiff',
    'success':   '/System/Library/Sounds/Glass.aiff',
    'celebrate': '/System/Library/Sounds/Ping.aiff',
    'menu':      '/System/Library/Sounds/Tink.aiff',
    'error':     '/System/Library/Sounds/Basso.aiff',
}

def play(name):
    if sys.platform == 'darwin':
        try:
            subprocess.Popen(
                ['afplay', _SOUNDS.get(name, _SOUNDS['menu'])],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except Exception:
            pass

# ── 工具函数 ───────────────────────────────────────────────────────────────────
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def typewriter(text, color=W, delay=0.025):
    for ch in text:
        print(color + ch + RST, end='', flush=True)
        time.sleep(delay)
    print()

def loading_bar(duration=1.0, label='处理中'):
    W2 = 28
    for i in range(W2 + 1):
        filled  = '█' * i
        empty   = '░' * (W2 - i)
        pct     = int(i / W2 * 100)
        print(f'\r  {C}{label} [{G}{filled}{DIM}{empty}{C}] {Y}{pct:>3}%{RST}',
              end='', flush=True)
        time.sleep(duration / W2)
    print(f'  {G}✓{RST}')

def progress_bar(value, max_val, width=22, color=G):
    filled = int(value / max(max_val, 1) * width)
    return f'{color}{"█" * filled}{DIM}{"░" * (width - filled)}{RST}'

def sparkle_line(times=3):
    frames = ['✨  🌟  💫  ⭐  🌟  ✨',
              '🌟  ✨  ⭐  💫  ✨  🌟',
              '💫  🌟  ✨  ⭐  🌟  💫']
    for _ in range(times):
        for f in frames:
            print(f'\r  {f}', end='', flush=True)
            time.sleep(0.12)
    print()

# ── 标题 ───────────────────────────────────────────────────────────────────────
HEADER = [
    '╔══════════════════════════════════════════════════════════════╗',
    '║  ██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗               ║',
    '║  ██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║               ║',
    '║  ██║     █████╗  ███████║██████╔╝██╔██╗ ██║               ║',
    '║  ██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║               ║',
    '║  ███████╗███████╗██║  ██║██║  ██║██║ ╚████║               ║',
    '║  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝               ║',
    '║                                                              ║',
    '║           📚   学 习 进 度 追 踪 器   v1.0   📚              ║',
    '╚══════════════════════════════════════════════════════════════╝',
]

def print_header():
    clear()
    for i, line in enumerate(HEADER):
        print(PALETTE[i % len(PALETTE)] + BD + line + RST)
        time.sleep(0.02)

# ── 数据层 ─────────────────────────────────────────────────────────────────────
def load_records():
    p = Path(RECORDS_FILE)
    if p.exists():
        with open(p, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_records(records):
    with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

# ── 功能 1：添加记录 ───────────────────────────────────────────────────────────
def add_record():
    print_header()
    print(f'\n{Y}{BD}  ╔═══════════════════════════════════╗')
    print(f'  ║   ✏️   添加今日学习记录            ║')
    print(f'  ╚═══════════════════════════════════╝{RST}\n')

    today   = datetime.date.today().strftime('%Y-%m-%d')
    records = load_records()

    today_list = [r for r in records if r['date'] == today]
    if today_list:
        print(f'  {Y}⚡ 今天已有 {BD}{len(today_list)}{RST}{Y} 条记录：{RST}')
        for r in today_list:
            print(f'    {G}▸ {r["content"]}{RST}')
        print()

    print(f'  {C}📅 日期: {W}{BD}{today}{RST}')
    print(f'  {C}💡 今天学了什么？{DIM}（输入 q 返回）{RST}')
    print(f'  {DIM}{"─" * 42}{RST}')

    content = input(f'  {G}▶ {RST}').strip()

    if content.lower() == 'q' or not content:
        print(f'\n  {Y}↩  已取消{RST}')
        time.sleep(0.8)
        return

    loading_bar(0.7, '保存中')
    play('success')

    records.append({
        'date':      today,
        'content':   content,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    })
    save_records(records)

    unique_days = len(set(r['date'] for r in records))

    print(f'\n  {G}{BD}╔═══════════════════════════════════╗{RST}')
    print(f'  {G}{BD}║  🎉 记录保存成功！                 ║{RST}')
    print(f'  {G}{BD}║  📊 累计学习: {Y}{unique_days:<4}{G} 天               ║{RST}')
    print(f'  {G}{BD}╚═══════════════════════════════════╝{RST}\n')

    if unique_days in (7, 14, 30, 60, 100):
        play('celebrate')
        print(f'\n  {Y}{BD}🏆 里程碑达成！已坚持 {unique_days} 天！{RST}')
        sparkle_line(3)

    time.sleep(1.5)

# ── 功能 2：查看记录 ───────────────────────────────────────────────────────────
def view_records():
    print_header()
    print(f'\n{B}{BD}  ╔═══════════════════════════════════╗')
    print(f'  ║   📖  所有学习记录                 ║')
    print(f'  ╚═══════════════════════════════════╝{RST}\n')

    play('menu')
    records = load_records()

    if not records:
        print(f'  {Y}📭 暂无记录，快去添加第一条学习记录吧！{RST}')
        time.sleep(1.5)
        return

    loading_bar(0.5, '加载中')

    grouped = {}
    for r in records:
        grouped.setdefault(r['date'], []).append(r['content'])

    colors = [C, M, Y, G, B]

    print(f'\n  {DIM}{"─" * 48}{RST}')
    for idx, date in enumerate(sorted(grouped.keys(), reverse=True)):
        dc = colors[idx % len(colors)]
        wd = ['周一','周二','周三','周四','周五','周六','周日'][
            datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        ]
        bullets = ['●', '◆', '▶', '★']

        print(f'\n  {dc}{BD}📅 {date}  {wd}{RST}')
        print(f'  {dc}╔{"═" * 44}╗{RST}')
        for j, content in enumerate(grouped[date]):
            b = bullets[j % len(bullets)]
            # 截断超长内容
            disp = content if len(content) <= 41 else content[:38] + '...'
            print(f'  {dc}║{RST} {W}{b} {disp:<42}{dc}║{RST}')
        print(f'  {dc}╚{"═" * 44}╝{RST}')
        time.sleep(0.04)

    total_days = len(grouped)
    total_rec  = len(records)
    print(f'\n  {DIM}{"─" * 48}{RST}')
    print(f'\n  {G}共 {Y}{BD}{total_days}{RST}{G} 天 · {Y}{BD}{total_rec}{RST}{G} 条记录{RST}\n')
    input(f'  {DIM}按 Enter 返回主菜单...{RST}')

# ── 功能 3：统计信息 ───────────────────────────────────────────────────────────
def show_stats():
    print_header()
    print(f'\n{M}{BD}  ╔═══════════════════════════════════╗')
    print(f'  ║   📊  学习统计                     ║')
    print(f'  ╚═══════════════════════════════════╝{RST}\n')

    play('menu')
    records = load_records()

    if not records:
        print(f'  {Y}📭 暂无记录{RST}')
        time.sleep(1.5)
        return

    loading_bar(0.6, '计算中')

    unique_days  = len(set(r['date'] for r in records))
    total_rec    = len(records)
    dates_sorted = sorted(set(r['date'] for r in records))

    # 连续天数
    max_streak = cur = 1
    for i in range(1, len(dates_sorted)):
        d1 = datetime.datetime.strptime(dates_sorted[i-1], '%Y-%m-%d').date()
        d2 = datetime.datetime.strptime(dates_sorted[i],   '%Y-%m-%d').date()
        if (d2 - d1).days == 1:
            cur += 1
            max_streak = max(max_streak, cur)
        else:
            cur = 1

    # 当前连续（末尾日期与今天/昨天相邻则算）
    today_date = datetime.date.today()
    last_date  = datetime.datetime.strptime(dates_sorted[-1], '%Y-%m-%d').date()
    if (today_date - last_date).days > 1:
        current_streak = 0
    else:
        current_streak = 1
        for i in range(len(dates_sorted) - 1, 0, -1):
            d1 = datetime.datetime.strptime(dates_sorted[i-1], '%Y-%m-%d').date()
            d2 = datetime.datetime.strptime(dates_sorted[i],   '%Y-%m-%d').date()
            if (d2 - d1).days == 1:
                current_streak += 1
            else:
                break

    # 等级
    def get_level(days):
        if days >= 100: return ('💎 钻石学者', M)
        if days >= 60:  return ('🏅 黄金学者', Y)
        if days >= 30:  return ('🥈 白银学者', W)
        if days >= 14:  return ('🥉 青铜学者', C)
        if days >= 7:   return ('🌱 成长之星', G)
        return               ('🔰 初学者',   DIM + W)

    level_name, level_color = get_level(unique_days)

    print(f'\n  {DIM}{"═" * 48}{RST}')
    print(f'  {BD}{level_color}  当前等级: {level_name}{RST}')
    print(f'  {DIM}{"═" * 48}{RST}\n')

    stats = [
        ('📅 总学习天数',   unique_days,     100, C),
        ('📝 总记录条数',   total_rec,       200, Y),
        ('🔥 当前连续天数', current_streak,   30, R),
        ('🏆 最长连续天数', max_streak,       30, M),
    ]
    for label, val, maxv, color in stats:
        bar = progress_bar(val, maxv, 22, color)
        print(f'  {W}{label}:{RST}')
        print(f'  {bar} {color}{BD}{val}{RST}\n')
        time.sleep(0.15)

    # 最近 7 天热力图
    rec_count = {}
    for r in records:
        rec_count[r['date']] = rec_count.get(r['date'], 0) + 1

    print(f'  {C}📆 最近 7 天热力图:{RST}\n  ', end='')
    days7 = [today_date - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    for d in days7:
        cnt = rec_count.get(d.strftime('%Y-%m-%d'), 0)
        if   cnt == 0: print(f'{DIM}░░{RST}', end=' ')
        elif cnt == 1: print(f'{G}▒▒{RST}', end=' ')
        elif cnt == 2: print(f'{G}▓▓{RST}', end=' ')
        else:          print(f'{G}██{RST}', end=' ')
    print()

    print('  ', end='')
    wd_names = ['一','二','三','四','五','六','日']
    for d in days7:
        print(f'{DIM}周{wd_names[d.weekday()]}{RST}', end=' ')
    print(f'\n\n  {DIM}░░=无  ▒▒=1条  ▓▓=2条  ██=3条+{RST}\n')
    print(f'  {DIM}{"═" * 48}{RST}')

    input(f'\n  {DIM}按 Enter 返回主菜单...{RST}')

# ── 主菜单 ─────────────────────────────────────────────────────────────────────
def main():
    play('start')

    while True:
        print_header()

        today   = datetime.date.today().strftime('%Y-%m-%d')
        records = load_records()
        unique_days  = len(set(r['date'] for r in records))
        today_count  = sum(1 for r in records if r['date'] == today)

        print(f'\n  {DIM}{"─" * 56}{RST}')
        print(f'  {C}今日: {W}{BD}{today}{RST}  '
              f'{G}累计: {Y}{BD}{unique_days} 天{RST}  '
              f'{B}今日: {Y}{BD}{today_count} 条{RST}')
        print(f'  {DIM}{"─" * 56}{RST}\n')

        menu = [
            ('1', '✏️   添加今日学习记录', G),
            ('2', '📖  查看所有学习记录', B),
            ('3', '📊  查看学习统计',     M),
            ('0', '👋  退出',             R),
        ]
        for key, label, color in menu:
            print(f'  {color}{BD}[{key}]{RST}  {W}{label}{RST}')

        print(f'\n  {DIM}{"─" * 56}{RST}')
        choice = input(f'\n  {Y}▶ 请选择 (0-3): {RST}').strip()

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            show_stats()
        elif choice == '0':
            play('menu')
            print_header()
            print()
            typewriter('  感谢使用！坚持学习，每天进步一点点 🚀', C, 0.04)
            print()
            time.sleep(1)
            sys.exit(0)
        else:
            play('error')
            print(f'\n  {R}❌ 无效选择，请重试{RST}')
            time.sleep(0.7)


if __name__ == '__main__':
    main()
