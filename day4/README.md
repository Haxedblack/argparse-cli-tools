# 🪵 LogParse CLI Tool

A flexible, beginner-friendly CLI tool to parse and analyze structured `.log` or `.txt` files.  
Built with Python’s `argparse` and colorized using `colorama`.

---

## 🚀 Features

- 🔍 Filter log entries by date (`--date`) or log level (`--level`)
- 🔢 Count matching lines using `--count`
- 📊 Generate a level-wise summary of logs for a specific date using `--summary`
- 🖨️ Print raw matching log lines to the terminal

---

## 🧾 Expected Log Format

Each log entry must follow this format:

```
YYYY-MM-DD HH:MM:SS LEVEL Message text here...
```

📌 Example:
```
2023-07-01 09:00:00 INFO Boot sequence initialized
2023-07-01 10:00:00 ERROR Database connection failed
2023-07-02 11:30:00 WARN Memory usage high
```

---

## 🧪 Example Usage

### ✅ Count logs matching a date and level
```bash
python day4/logparse.py --file day4/sample.log --date 2023-07-01 --level ERROR --count
```
Output:
```
Found 2 matching lines.
```

---

### ✅ Show all WARN logs
```bash
python day4/logparse.py --file day4/sample.log --level WARN
```
Output:
```
2023-07-02 11:30:00 WARN Memory usage high
```

---

### ✅ Show all logs on a date
```bash
python day4/logparse.py --file day4/sample.log --date 2023-07-01
```

---

### ✅ Show summary for a date
```bash
python day4/logparse.py --file day4/sample.log --date 2023-07-01 --summary
```
Output:
```
INFO: 1
WARN: 1
ERROR: 2
```

---

## 📁 File Structure

```
argparse-cli-tools/
├── day4/
│   ├── logparse.py       # ✅ The CLI tool
│   ├── sample.log        # ✅ Test log file
│   └── README.md         # 📄 You're here
```

---

## 🎨 CLI Flags

| Flag         | Type     | Description                                 |
|--------------|----------|---------------------------------------------|
| `--file`     | `str`    | Path to the `.log` file                     |
| `--date`     | `str`    | Filter entries by date (e.g., 2023-07-01)  |
| `--level`    | `str`    | Filter entries by log level (e.g., ERROR)  |
| `--count`    | `flag`   | Count matching entries                      |
| `--summary`  | `flag`   | Show level-wise count for a given date     |

📌 `--count` and `--summary` are **mutually exclusive** (you must use only one at a time).

---

## 🧠 Notes

- Case-insensitive log level matching (e.g., `error`, `ERROR`, `Error` all work)
- Whitespace is trimmed automatically
- Only one of `--count` or `--summary` can be used at a time

---

## 👨‍💻 Author

**Harshit Singh**  
GitHub: [@Haxedblack](https://github.com/Haxedblack)

---

## ✅ License

MIT — use it, modify it, share it freely.
