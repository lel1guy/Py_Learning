# Simple To DO List
#Goal: Add, Track and mark tasks as complete
#Step:1. Have a list containing all the Tasks
#     2.Have a Menu where you can check,add ou mark as complete the tasks1

tasks = []

while True:

    # The Menu
    print("=" * 50)
    print("Welcome to you To Do List!")
    print("-" * 50)
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Quit")

    choice = input("Make Your Choice (1/2/3/4): ")

    if choice == "1":
        print("=" * 50)
        print("\n --- Your Tasks ---")
        if not tasks:
            print("You got no Tasks!")
        else:
            for index, task_item in enumerate(tasks, start=1):
                status = "✓" if task_item["completed"] else " "
                print(f"{index}. [{status}] {task_item['task']}")
    elif choice == "2":
        new_task_description = input("Enter a new task: ")
        new_task = {"task": new_task_description, "completed": False}
        tasks.append(new_task)
        print("New Task Added!, Let's get to Work!")

    elif choice == "3":
        if not tasks:
            print("You got no Tasks!")
            continue

        print("\n --- Your Tasks ---")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")
        try:
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == "4":
        print("GoodBye! Hope to see you next time!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")