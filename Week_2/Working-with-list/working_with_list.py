# How to Create a list
# You can create an empty list when you don't have elements yet but plan to add later.

#method 1: Using square brackets
empty_list = []
print(empty_list) #Output: []

#Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)  # Output: []



# Creating a List with Initial Elements.
# Lists can store multiple items separated by commas inside square brackets.

# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers) # Output: [ 1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list) # output: ['Alice', 25, 5.8, True]



# Creating a List from Another Sequence. You can convert strings, tuples, or other iterables into a list.
# From a string (each character becomes an element)
chars = list("hello")
print(chars) # Output: ['h', 'e', 'l', 'l', 'o'

# From a tuple
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple) # Output: [10, 20, 30]



# FROM A RANGE
numbers_range = list(range(5))
print(numbers_range) # Output: [0, 1, 2, 3, 4]



#  Creating a List Using List Comprehension. 
# List comprehensions are a concise way to create lists using a loop in one line.
# *We will come back to this later*



# Squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)


# Even numbers between 0–10
evens = [x for x in range(11) if x % 2 == 0]
print(evens) # Output: [0, 2, 4, 6, 8, 10]




# - Creating a Nested List. A list can contain other lists  It is useful for matrices or grouped data.
# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix) # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing element in nested list
print(matrix[0]) # Output: [1, 2]
print(matrix[0][1])



# Characteristics of a list


# 1. Ordered Collection

# - The elements in a list maintain the order in which they are inserted.

# - The first element has index 0, the second has index 1, and so on.

fruits = ["mango", "orange", "banana"]
print(fruits)           # ['mango', 'orange', 'banana']
print(fruits[0])        # mango (first element)
print(fruits[2])      # banana (third element)



# 2. Allows Duplicates

# - Lists can store the same value multiple times.
items = ["rice", "beans", "yam", "rice"]
print(items) # ['rice', 'beans', 'yam', 'rice']



# 3. Mutable (Can Be Changed)
# - You can modify a list after it’s created—change elements, add new ones, or remove existing ones.
numbers = [1, 2, 3]
numbers[1] = 20     # Changing element at index 1
print(numbers)      # [1, 20, 3]




# 4. Can Contain Different Data Types
# - A list can hold integers, strings, floats, booleans, and even other lists.
mixed = [10, "Nigeria", 3.14, True]
print(mixed)  # [10, 'Nigeria', 3.14, True]




# 5. Can Be Nested
# - A list can contain other lists (2D or multi-dimensional lists).
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)       # [[1, 2], ['a', 'b']]
print(nested_list[0][1]) # 2





# 6. Dynamic Size
# - You don’t need to declare the size of a list beforehand; it can grow or shrink as needed.
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)