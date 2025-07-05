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
| `day4/` | Log file parser with filtering by `--date` and `--level`, plus `--count` and `--summary` options |

---

## ✅ Features

- Positional and optional argument parsing
- Mutually exclusive groups (e.g., `--minutes` vs `--seconds`)
- Subcommands via `argparse` subparsers
- Clean modular folder structure (per day/tool)
- Git-tracked daily development history
- Real-time CLI behavior using `time.sleep()` and `colorama` styling
- Beginner-friendly structure for learning and experimentation

---

## 🚀 Getting Started

Clone the repo:

```bash
git clone https://github.com/Haxedblack/argparse-cli-tools.git
cd argparse-cli-tools
```

Run individual tools:

---

### 📌 Day 1 – Calculator

```bash
cd day1
python calc.py 5 3 --opp sub --verbose
```

---

### 📌 Day 2 – To-Do CLI

```bash
cd day2
python todo.py add "Buy groceries"
python todo.py list
```

---

### 📌 Day 3 – Countdown Timer

```bash
cd day3
python timer.py --seconds 5 --verbose --message "⏰ Time's up!"
```

---

### 📌 Day 4 – Log File Parser

```bash
cd day4
python logparse.py --file sample.log --date 2023-07-01 --level ERROR --count
```

Other examples:

```bash
python logparse.py --file sample.log --level WARN
python logparse.py --file sample.log --date 2023-07-01 --summary
```

---

## 👨‍💻 Author

**Harshit Singh**  
GitHub: [@Haxedblack](https://github.com/Haxedblack)

---

## ✅ License

MIT — use it, fork it, or build upon it freely.
