import json
import os

FILE_PATH = 'todo.txt'


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=2)


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")


def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Completed: {tasks.pop(index)}")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


def clear_tasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        save_tasks([])
        print("All tasks cleared.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO MENU ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task done")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            clear_tasks()
            tasks = []
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
