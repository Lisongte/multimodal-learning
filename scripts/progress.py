#!/usr/bin/env python3
"""Create a daily progress note without replacing an existing file."""
import argparse
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", type=date.fromisoformat, help="YYYY-MM-DD; defaults to Asia/Shanghai today")
    args = parser.parse_args()
    day = args.date or datetime.now(ZoneInfo("Asia/Shanghai")).date()
    root = Path(__file__).resolve().parents[1]
    path = root / "progress" / f"{day:%Y-%m}" / f"{day.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"""# {day.isoformat()} 学习记录

- 计划用时：
- 实际用时：
- 本周目标：

## 实际完成

- [ ] 填写真实完成的任务，未完成的不勾选。

## 代码与实验依据

- 文件/命令：
- 实际结果：

## 今天能独立解释什么

-

## 问题与解决过程

- 现象：
- 原因/假设：
- 排查与验证：

## AI 辅助与独立完成部分

- AI 辅助：
- 自己实现/修改/验证：

## 下一步

-
"""
    try:
        with path.open("x", encoding="utf-8") as stream:
            stream.write(content)
        print(f"Created: {path}")
    except FileExistsError:
        print(f"Already exists (unchanged): {path}")


if __name__ == "__main__":
    main()
