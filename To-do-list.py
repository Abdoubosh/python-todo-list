try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    print("\n1-Add task")
    print("2-View tasks")
    print("3-Delete task")
    print("4-Delete all tasks")
    print("5-Exit")

    choice = input("Choose an option?")

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            save_tasks()
            print("Task added")
        else:
            print("Task cannot be empty")

    elif choice == "2":
        if not tasks:
            print("There are no tasks yet")
        else:
            for i, task in enumerate (tasks, 1):
                print(i, "-", task)
    
    elif choice == "3":
        if not tasks:
            print("There are no tasks to delete")
        else:
            for i, task in enumerate (tasks, 1):
                print(i, "-", task)
            while True:
                task_choice = input("Choose a task number to delete or type 'exit' to exit: ").strip().lower()
                if task_choice == "exit":
                    break
                try:
                    task_number = int(task_choice)
                    if 1 <= task_number <= len(tasks):
                        tasks.pop(task_number -1)
                        save_tasks()
                        print("Task deleted")
                        if not tasks:
                            print("No tasks left")
                        else:
                         for i, task in enumerate (tasks, 1):
                            print(i, "-", task)
                        break
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a valid number")

    elif choice == "4":
        if not tasks:
            print("There are no tasks to delete")
        else:
            for i, task in enumerate (tasks, 1):
                print(i, "-", task)
            confirmation = input("Type 'confirm' to confirm ").strip().lower()
            if confirmation == "confirm":
                tasks.clear()
                save_tasks()
                print("All tasks deleted")
            else:
                print("Deletion cancelled")

    elif choice == "5":
        break
    else:
        print("Invalid choice.")

    input("\nPress enter to continue")
