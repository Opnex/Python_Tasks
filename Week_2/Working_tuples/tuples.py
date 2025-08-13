#TUPLES
# A tuple is an ordered, immutable (unchangeable) collection of items in Python.

#Creating Tuples
#1. Using parentheses
# Example: tuple with multiple items
fruits = ("apple", "banana", "cherry")
print(fruits) # Output: ('apple', 'banana', 'cherry')




#2. Without parentheses (tuple packing)
number = 1, 2, 3
print(number) # Output: (1, 2, 3)



#3. Single-item tuple (must include a comma)

single_item = ("apple")
print(single_item) # Output: apple

single_item = ("apple",)
print(single_item) # Output: ('apple',)
print(type(single_item)) # Output: <class 'tuple'>



#4. Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)   #('apple', 'banana', 'cherry')



#Characteristics of Tuples
# 1. Ordered – Items have a fixed position.
# 2. Immutable – Cannot change after creation.
# 3. Allow duplicates – Same value can appear multiple times.
# 4. Can contain mixed data types – Strings, integers, lists, etc.
# 5. Can be nested – Tuples inside tuples.

#Order
colors = ("red", "green", "blue")
print(colors[0]) # Output: red


# Immutable ( uncomment and run. This will cause an error)
# colors[1] = "yellow"  # Output: TypeError



# Allow duplicates
numbers = (1, 2, 2, 3,)
print(numbers)   # Output: (1, 2, 2, 3)



# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed) # Output: ('apple', 3, True, 5.6)




# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested) # Output: (('a', 'b'), (1, 2))




# Tuple Operations
# - Even though tuples are immutable, you can still perform several operations

#1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])   # Output: banana
print(fruits[-1])  # Output: cherry



# 2. Slicing
print(fruits[0:2])     # Output: ('apple', 'banana')
print(fruits[::-1])    # Output: ('cherry', 'banana', 'apple')



# 4. Repetition
nums = (1, 2)
print(nums * 3) # Output: (1, 2, 1, 2, 1, 2)



# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)      # Output: True   
print("grape" not in fruits)   # Output: True    



# 6. Iteration
for fruit in fruits:
    print(fruit)



#Working with Tuples
# - You can’t modify a tuple directly, but you can
# - Convert it to a list, modify it, then convert back.
# - Use built-in functions to work with tuple contents.



# 1. Unpacking Tuples
person = ("John", 25, "Nigeria")
name, age, country = person
print(name)       # Output: John
print(age)        # Output: 25
print(country)    # Output: Nigeria



# Tuple Methods
# - Tuples have only two methods.

# dont count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(1))  # 2  (counts occurrences of 2)
print(numbers.index(3))  # 3 (position of first occurrence of 3)



# Converting Between List and Tuple
# Tuple to List
t = (1, 2, 3,)
lst = list(t)
lst.append(4)
print(lst) # [1, 2, 3, 4]


# List back to Tuple
t = tuple(lst)
print(t) # [1, 2, 3, 4]




# Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))  # 4
print(max(nums))  # 7
print(min(nums))  # 1
print(sum(nums))  # 15