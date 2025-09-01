# @title 2. To-Do List Application

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


# Simple To-Do List Application

import json

# List to store tasks

tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Tasks "{task}" added!')

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

# Function to display all tasks
def view_tasks():
    if tasks:
        print("Your Tasks: ")
        for idx, task in enumerate(tasks, 1):
            print(f'{idx}. {task}')
    else:
        print("No tasks in your list!")

        
# Infinite loop to keep the program running until user exits
while True:
    print("\nOptions: \n 1. Add Task \n 2. Remove Task  \n 3. View Tasks  \n 4. Exit")

    # Ask user for their choice
    choice = input("Enter your choice: ")

    if choice ==  '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice ==  '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Existing programe. Have a productive day!")
        break
    else:
        print("Invalid choice! Please select a valid a valid option")


def save_task(task, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(task, f)


def load_task(filename="tasks.json"):
        try:
            with open(filename, "r")as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
