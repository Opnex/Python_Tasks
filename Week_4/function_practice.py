def greet():
    print("Hello, welcome to AI Fellowship!")
greet()
greet()
greet()



# Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to Python learning!")

greet("Class rep")
greet("Ridwan")


#print function
def greet(name):
    print("Hello", name)

#function call
result = greet("Opeyemi")

# You will notice that it did not store the name
print("The result is:", result)  # The result is: None


#return function
def add(a, b):
    return a + b

#function call
result = add(4, 6)
print("The sum of 4 and 6 is:", result)  # The sum of 4 and 6 is: 10



#yield function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)  # Outputs: 1, 2, 3, 4, 5



#1. Positional Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

#function call
introduce("Malik", "AI Developer")

# Change the arrangment and watch the output
introduce("AI Developer", "Malik")


#2. Keyword Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

#function call
introduce(name = "Malik", track = "AI Developer")

# Change the arrangment and watch the output
introduce(track = "AI Developer", name = "Malik")



#3. Default Arguments
def introduce(name, track="AI Developer"):
    print("My name is", name)
    print("I am learning", track, ".")

#function call
# Without specifying the default argument, but watch the ouput
introduce("Malik")

# Specify the default argument and watch the output
introduce("Tunji Paul", track = "AI Development")


#4. Varying Length Arguments
#a. non-keyword (tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum: ", total)

#function call
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50) 