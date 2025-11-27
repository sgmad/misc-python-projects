tasks = []

while True:
    print("\n==== TO-DO LIST MENU ====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nYour to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter a new task: ").strip()
        if new_task:
            tasks.append(new_task)
            print(f"Task '{new_task}' added.")
        else:
            print("\nNo task entered. Nothing added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("\nYour to-do list is empty.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to edit: "))
                if 1 <= task_num <= len(tasks):
                    new_text = input("Enter the new task: ").strip()
                    if new_text:
                        old_task = tasks[task_num - 1]
                        tasks[task_num - 1] = new_text
                        print(f"Task '{old_task}' updated to '{new_text}'.")
                    else:
                        print("No new text entered. Task not changed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("\nYour to-do list is empty.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")