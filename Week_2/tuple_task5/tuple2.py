friends_names = [
    input("Please enter your 1st friend's name: "),
    input("Please enter your 2nd friend's name: "),
    input("Please enter your 3rd friend's name: "),
    input("Please enter your 4th friend's name: "),
    input("Please enter your 5th friend's name: ")
]
friends = tuple(friends_names)
print(friends[::-1])