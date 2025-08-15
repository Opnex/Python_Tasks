# Task2: Unique Name Collector
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
# students = {
#     input("please enter your full name: "),
#     input("please enter your full name: "),
#     input("please enter your full name: "),
#     input("please enter your full name: "),
#     input("please enter your full name: ")
# }
# print(f"Unique names: {sorted(students)}")

# Alternative approach using a loop
students = set()
for i in range(5):
    name = input("Please enter your full name: ")
    students.add(name)
    print(f"Unique nammes: {sorted(students)}")