"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""


TASKS_FILE = "Task.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

def add_task(task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number")


def view_task():
    if tasks:
        print("\nTask List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks in your list.")

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")

    choice = input("Please select your option (1/2/3): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)

    elif choice == '2':
        view_task()
        try:
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(index)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '3':     
        view_task()

    else:
        print("Invalid choice! Please select a valid option.")

    more_task = input("\nDo you want to perform more operations? (yes/no): ").strip().lower()
    if more_task != "yes":
        print("Thanks! Your operations were performed successfully.")
        break
