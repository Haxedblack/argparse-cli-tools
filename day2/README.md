# ✅ Day 2 - Todo CLI Tool

A simple, functional command-line todo manager built in Python using `argparse` and `json`.  
This tool lets you add tasks, list them, and mark them as complete — all from the terminal.

---

## 🧠 Features

- Add new tasks via command line
- View all tasks with status indicators (✅ done / ⏳ pending)
- Mark specific tasks as completed
- Data is persisted in `tasks.json`

---

## 💻 Usage

```bash
# Add a new task
python todo.py add "Learn argparse"

# List all tasks
python todo.py list

# Mark task #2 as done
python todo.py done 2
