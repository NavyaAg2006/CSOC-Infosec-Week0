import json
import os

FILE_PATH = 'todo.txt'

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return {"default": data}
            return data
        except json.JSONDecodeError:
            return {}

def save_tasks(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=2)

def list_tasks(user, data):
    tasks = data.get(user, [])
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(user, data):
    task = input("Enter new task: ").strip()
    if task:
        data.setdefault(user, []).append(task)
        save_tasks(data)
        print("Task added.")

def complete_task(user, data):
    tasks = data.get(user, [])
    list_tasks(user, data)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Completed: {tasks.pop(index)}")
            data[user] = tasks
            save_tasks(data)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def clear_tasks(user, data):
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == 'y':
        data[user] = []
        save_tasks(data)
        print("All tasks cleared.")

def select_user(data):
    users = list(data.keys())
    if users:
        print("\nAvailable users:")
        for i, u in enumerate(users, 1):
            print(f"{i}. {u}")
    else:
        print("No users found. Please create a new user.")

    while True:
        choice = input("Enter username or type 'new' to add a user: ").strip()
        if choice.lower() == 'new':
            new_user = input("Enter new username: ").strip()
            if new_user and new_user not in data:
                data[new_user] = []
                save_tasks(data)
                return new_user
            else:
                print("Invalid or duplicate username.")
        elif choice in data:
            return choice
        else:
            print("User not found. Try again or type 'new'.")

def rename_user(current_user, data):
    new_name = input(f"Enter new name for user '{current_user}': ").strip()
    if new_name and new_name not in data:
        data[new_name] = data.pop(current_user)
        save_tasks(data)
        print(f"Username changed to '{new_name}'.")
        return new_name
    else:
        print("Invalid or duplicate username.")
        return current_user

def delete_user(current_user, data):
    confirm = input(f"Are you sure you want to delete user '{current_user}' and all tasks? (y/n): ").lower()
    if confirm == 'y':
        data.pop(current_user, None)
        save_tasks(data)
        print(f"User '{current_user}' deleted.")
        return select_user(data)
    else:
        print("User deletion canceled.")
        return current_user

def main():
    data = load_tasks()
    current_user = select_user(data)

    while True:
        print(f"\n--- TO-DO MENU ({current_user}) ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task done")
        print("4. Clear all tasks")
        print("5. Switch user")
        print("6. Rename user")
        print("7. Delete user")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip()
        if choice == '1':
            list_tasks(current_user, data)
        elif choice == '2':
            add_task(current_user, data)
        elif choice == '3':
            complete_task(current_user, data)
        elif choice == '4':
            clear_tasks(current_user, data)
        elif choice == '5':
            current_user = select_user(data)
        elif choice == '6':
            current_user = rename_user(current_user, data)
        elif choice == '7':
            current_user = delete_user(current_user, data)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
