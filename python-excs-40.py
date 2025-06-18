tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number.")

def mark_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("Invalid task number.")

def show_tasks():
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['task']}")

# Simple menu to use the to-do list
while True:
    print("\n1. Add Task\n2. Remove Task\n3. Mark Task Complete\n4. Show Tasks\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        t = input("Enter task: ")
        add_task(t)
    elif choice == "2":
        show_tasks()
        i = int(input("Enter task number to remove: "))
        remove_task(i)
    elif choice == "3":
        show_tasks()
        i = int(input("Enter task number to mark complete: "))
        mark_complete(i)
    elif choice == "4":
        show_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
