five_state = [
    input("Please enter your 1st state: "),
    input("Please enter your 2nd state: "),
    input("Please enter your 3rd state: "),
    input("Please enter your 4th state: "),
    input("Please enter your 5th state: ")
]
states = tuple(five_state)
print(states[0])
print(states[-1])
print("Lagos" in states)
print(len(states))
