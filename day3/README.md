# ⏱️ Countdown Timer CLI

A simple countdown timer built using Python's `argparse` module.  
Supports countdown in either minutes or seconds, with optional verbose output and custom message display.

---

## 🚀 Features

- ⏳ Countdown timer with real-time updates
- 🛠️ Mutually exclusive flags for `--minutes` and `--seconds`
- 💬 Optional `--message` to display at the end
- 🗣️ Optional `--verbose` to show start and end messages
- ✅ Clean output with time formatting (`MM:SS`)
- 🧪 Great example of using `argparse` for real-world scripting

---

## 📦 Usage

### ⬇️ Run from repo root:
```bash
cd day3
python timer.py --seconds 5 --verbose --message "⏰ Time's up!"
