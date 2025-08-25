# Defining a function
def greet():
    print("Hello, welcome to AI Fellowship")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()



# Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "Welcome to Python learning")

# Calling with parameter- the actual name
greet("Class Rep")
greet("Ridwan")



# print()
def greet(name):
    print("Hello", name)

# Function call    
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)


# return
def add(a, b):
    return a + b

# Function call
result = add (4, 6)
print("The sum is: ", result)