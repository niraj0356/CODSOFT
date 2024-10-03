tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    display_tasks()
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task removed.")
    else:
        print("Invalid task number.")

def update_task():
    display_tasks()
    task_num = int(input("Enter the task number to update: "))
    if 0 < task_num <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_num - 1] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Display Tasks\n2. Add Task\n3. Remove Task\n4. Update Task\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        display_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        update_task()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
