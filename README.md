# 🛠️ argparse-cli-tools

A collection of command-line utilities built using Python's `argparse` module.  
Each subfolder (`day1/`, `day2/`, etc.) contains a focused CLI tool that demonstrates real-world usage of Python CLI scripting.

---

## 📁 Folder Structure

| Folder | Description |
|--------|-------------|
| `day1/` | CLI calculator with `--opp`, `--verbose`, and `--round` flags |
| `day2/` | Todo list manager with `add`, `list`, and `done` commands |

---

## ✅ Features

- Positional and optional argument parsing
- Subcommands using `argparse` subparsers
- Clean modular folder structure (per day/tool)
- Git-tracked development history
- Built for beginner-to-intermediate CLI scripting proficiency

---

## 🚀 Getting Started

Clone the repo:

```bash
git clone https://github.com/Haxedblack/argparse-cli-tools.git
cd argparse-cli-tools/day1
python calc.py 5 3 --opp sub --verbose
