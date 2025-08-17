# **Task1: Student Bio Data Storage**
# - Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
# - Courses should be stored as a list.
# - Display the bio-data neatly using escape sequences.
# - Requirements:
# - Use `input()` to collect details.
# - Use dictionary operations `(dict[key] = value)` to store data.
# - Use `print()` formatting with `\n` and `\t` for better output.

# Student Bio Data Storage

student = {}

# Collect details
student['name'] = input("Enter student's name: ")
student['age'] = int(input("Enter student's age: "))
student['gender'] = input("Enter student's gender: ")
courses = input("Enter courses (comma-separated): ")
student['courses'] = [course.strip() for course in courses.split(",")]

# Display bio-data neatly
print("\n\t=== STUDENT BIO DATA ===")
print(f"Name:\t\t{student['name']}")
print(f"Age:\t\t{student['age']}")
print(f"Gender:\t\t{student['gender']}")
print(f"Courses:\t{', '.join(student['courses'])}")