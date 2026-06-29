# ==========================================
#        CODSOFT - TO DO LIST
#        Developed by: Priyanshu
# ==========================================

import os

TASK_FILE = "tasks.txt"


# Load Tasks
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []


# Save Tasks
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()

while True:

    print("\n" + "=" * 45)
    print("          TO-DO LIST MANAGER")
    print("=" * 45)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("\nChoose an Option (1-4): ")

    # Add Task
    if choice == "1":

        task = input("Enter New Task: ")

        tasks.append(task)

        save_tasks(tasks)

        print("\n✅ Task Added Successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:

            print("\nNo Tasks Available.")

        else:

            print("\nYour Tasks:\n")

            for i, task in enumerate(tasks, start=1):

                print(f"{i}. {task}")

    # Remove Task
    elif choice == "3":

        if len(tasks) == 0:

            print("\nNo Tasks Available.")

        else:

            print("\nYour Tasks:\n")

            for i, task in enumerate(tasks, start=1):

                print(f"{i}. {task}")

            try:

                task_no = int(input("\nEnter Task Number to Remove: "))

                if 1 <= task_no <= len(tasks):

                    removed = tasks.pop(task_no - 1)

                    save_tasks(tasks)

                    print(f"\n✅ '{removed}' Removed Successfully!")

                else:

                    print("\n❌ Invalid Task Number.")

            except ValueError:

                print("\n❌ Please Enter a Valid Number.")

    # Exit
    elif choice == "4":

        print("\nThank You for Using To-Do List ❤️")

        break

    else:

        print("\n❌ Invalid Choice. Please Try Again.")