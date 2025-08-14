# List Method
# Python provides many built-in methods for working with lists. 
# Here is each method, what it does and an example



# 1. Dot. append() method
# Adds an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)


# 2. Dot insert() method
# inserts an element at a sspecific position
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)



# 3. extend() method
# adds elememts from another list (or iterable) to the end.
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)



# 4. remove() method
# Removes the first occurence of specifild value.
fruits = {"apple", "banana", "cherry", "banana"}
fruits.remove("banana")
print(fruits)



# 5. dot pop() method
# removes and returns the element at a given index (default:last).
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)


# 6. dot clear() method
# remove all elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)



# 7. dot index() method
# return the index of the first occurence of aa value.
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)




# 8. dot count() method
# counts how many times a value appears.
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))




# 9. dot sort() method
# sorts the list in ascending order (default)
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)




# descending order
numbers.sort(reverse=True)
print(numbers)




# 10. dot reverse() method
# reversesn the order of the list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)




# copy()
# returns a shallow copy of the list (this should be familiar already)
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)