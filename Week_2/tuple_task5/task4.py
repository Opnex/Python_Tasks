user_name = input("Please enter your 1st name: ")
age = int(input("Please enter your age: "))
colour = input("Please enter your favourite colour: ")
town = input("Please enter your Home town: ")
details = user_name, age, colour, town
detail = tuple(details)
print(f"My name is {user_name}\nI am {age} years old.\nMy favourite colour is {colour}.\nI hail from {town} town ")