# @tittle 1. Basic Calculator

"""
A basic calculator is one of the fundamental
projects in Python programming. It provides essential
arithmetic operations such as addition, subtraction,
multiplication, and division. Understanding how to
implement a calculator helps in learning user input
handling, conditional statements, and function creation in
Python.

Key Concepts of Basic Calculator in Python
 Arithmetic Operations:
 Addition ( + )
 Subtraction (- )
 Multiplication ( * )
 Division ( / )
 Modulus ( % )
 Exponentiation ( ** )
 User Input Handling:
 Using input() function
 Converting strings to integers or floats
 Functions in Python:
 Defining functions for calculations
 Calling functions with user inputs
 Error Handling:
 Parameter Table
 Operator
 Handling division by zero
 Handling invalid inputs
 """

# Simple Calculator Program

# import math

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error Division by zero"

# def sqr_root(a):
#     if a >= 0:
#         return math.sqrt(a)
#     else:
#         return "Error message"

# def power(a, b):
#     return a ** b

# while True:
#     # Display operation options
#     print("\nSelect operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Sqr root")
#     print("6. Exponentiation (x^y)")

#     choice = input("Enter choice (1/2/3/4/5/6): ")

#     if choice == '5':
#         num = float(input("Enter number: "))
#         print("Result: ", sqr_root(num))
#     else:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))
#         elif choice == '6':
#             print("Result: ", power(num1, num2))
#         else:
#             print("Invalid choice")

#     more = input("Do you want to perform more calculation: (yes/no) ").lower()
#     if more != "yes":
#         print("Goodbye!")
#         break



import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def sqr_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Cannot find square root of negative number"

def power(a, b):
    return a ** b

while True:
    # Display operation options
    print("\n" + "="*40)
    print("         Simple Calculator")
    print("="*40)
    print("1.  Add")
    print("2.  Subtract")
    print("3.  Multiply")
    print("4.  Divide")
    print("5.  Square Root")
    print("6.  Exponentiation (x^y)")
    print("="*40)

    choice = input(" Enter choice (1/2/3/4/5/6): ")

    print("\n" + "-"*40)
    if choice == '5':  # Square root requires one number
        num = float(input("Enter number: "))
        result = sqr_root(num)
        print(f" Result: {num} = {result}")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f" Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f" Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f" Result: {num1} × {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f" Result: {num1} ÷ {num2} = {result}")
        elif choice == '6':
            result = power(num1, num2)
            print(f" Result: {num1}^{num2} = {result}")
        else:
            print(" Invalid choice, please try again.")

    print("-"*40)

    more = input("\n Do you want to perform more calculations? (yes/no): ").lower()
    if more != "yes":
        print("\n" + "="*40)
        print(" Thanks for using the calculator. Goodbye!")
        print("="*40)
        break
