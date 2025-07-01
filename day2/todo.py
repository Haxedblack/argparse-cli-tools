import argparse
import json
from pathlib import Path
TASK_FILE = Path('day2/tasks.json')
def load_tasks():
    if TASK_FILE.exists():
        try:
            with open(TASK_FILE,'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []
def save_tasks(tasks):
    with open(TASK_FILE,'w') as f:
        json.dump(tasks, f, indent = 2)
def main():
    parser = argparse.ArgumentParser(description = 'Simple To-Do CLI')
    sub_parser = parser.add_subparsers(dest= 'command')

    add_parser = sub_parser.add_parser('add',help= 'Add a new task')
    add_parser.add_argument('task',help= 'Task Description')
    list_parser = sub_parser.add_parser('list',help = 'List all tasks')
    done_parser = sub_parser.add_parser('done',help = "Mark a task as done")
    done_parser.add_argument('num',type = int ,help = "Index of task done")
    
    args = parser.parse_args()
    if args.command == "add":
        tasks = load_tasks()
        tasks.append({'task': args.task , "done": False })
        save_tasks(tasks)
        print(f" Tasks added : {args.task} ")
    elif args.command == "list":
        tasks = load_tasks()
        if not tasks:
            print("No tasks added yet")
            return
        print("Your Tasks:")
        for idx,task in enumerate(tasks,1):
            status = "✅" if task.get("done") else "⏳"
            print(f"{idx}. {status} {task['task']}")
    elif args.command == 'done':
        tasks = load_tasks()
        if not tasks:
            print("No tasks to mark")
        if not (1 <= args.num <= len(tasks)):
            print(f"Invalid task number: {args.num}")
            return
        else:
            tasks[args.num - 1]["done"] = True
            print(f"✅ Marked task {args.num} as done: {tasks[args.num-1]['task']}")
            save_tasks(tasks)
if __name__ == '__main__':
    main()