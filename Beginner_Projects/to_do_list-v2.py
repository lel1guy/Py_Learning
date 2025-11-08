# Simple To DO List
#Goal: Add, Track and mark tasks as complete
#Step:1. Have a list containing all the Tasks
#     2.Have a Menu where you can check,add ou mark as complete the tasks1

def view_task(tasks):
    print("=" * 50)
    print("\n === Your Tasks ===")
    if not tasks:
        print("You go no Task, go set them uo!")
    else:
        for index, task_item in enumerate(tasks, start=1):
            status = "✓" if task_item["completed"] else " "
            print(f"{index}. [{status}] {task_item["task"]}")
    print("=" * 50)

def add_task(task):
    new_task_description = input("Enter a new task:")
    new_task = {"task" : new_task_description, "completed": False}
    task.append(new_task)
    print(f"task '{new_task_description}' added!")

def mark_task_complete(task):
    if not task:
        print("You aint got tasks to mark!")
        return
    view_task(task)
    try:
        task_number = int(input("ENter the task number to mark as complete: "))
        if 1 <= task_number <= len(task):
            task[task_number - 1]["completed"] = True
            print("Task done!!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Quit")

def main():
    tasks = []
    print("=" * 50)
    print("Welcome to your To Do List!")
    print("-" * 50)

    while True:
        show_menu()
        choice = input("Make Your Choice (1/2/3/4): ")

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("GoodBye! Hope to see you next time!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()


#