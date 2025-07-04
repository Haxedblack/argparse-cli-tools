## 🛠️ argparse-cli-tools

A collection of command-line utilities built using Python's `argparse` module.  
Each subfolder (`day1/`, `day2/`, etc.) contains a focused CLI tool demonstrating real-world usage of Python CLI scripting.

---

## 📁 Folder Structure

| Folder  | Description |
|---------|-------------|
| `day1/` | CLI calculator with `--opp`, `--verbose`, and `--round` flags |
| `day2/` | To-Do list manager with `add`, `list`, and `done` commands |
| `day3/` | Countdown timer with mutually exclusive `--minutes` / `--seconds`, `--verbose`, and `--message` options |

---

## ✅ Features

- Positional and optional argument parsing
- Mutually exclusive groups
- Subcommands via `argparse` subparsers
- Clean modular folder structure (per day/tool)
- Git-tracked daily development history
- Real-time CLI behavior using `time.sleep()`
- Built for beginner-to-intermediate CLI scripting proficiency

---

## 🚀 Getting Started

Clone the repo:

```bash
git clone https://github.com/Haxedblack/argparse-cli-tools.git
cd argparse-cli-tools
```

Run individual tools:

### Day 1 - Calculator
```bash
cd day1
python calc.py 5 3 --opp sub --verbose
```

### Day 2 - To-Do CLI
```bash
cd day2
python todo.py add "Buy groceries"
python todo.py list
```

### Day 3 - Countdown Timer
```bash
cd day3
python timer.py --seconds 5 --verbose --message "⏰ Time's up!"
```
