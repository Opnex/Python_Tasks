# **Task1: Fruit collector**
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

# fav_fruits = {
#     input("Please eneyter your 1st favourite fruit: "),
#     input("Please eneyter your 2nd favourite fruit: "),
#     input("Please eneyter your 3rd favourite fruit: "),
#     input("Please eneyter your 4th favourite fruit: "),
#     input("Please eneyter your 5th favourite fruit: ")
# }
# print(fav_fruits)

fav_fruits = set()
for i in range(5):
    fruits = input("Please enter your favourite fruit name: ")
    fav_fruits.add(fruits)
print(f"{fav_fruits}")



# Task2: Unique Name Collector
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
students = {
    input("please enter your full name: "),
    input("please enter your full name: "),
    input("please enter your full name: "),
    input("please enter your full name: "),
    input("please enter your full name: ")
}
alphabetical_order = list(students).sort()
print(alphabetical_order)