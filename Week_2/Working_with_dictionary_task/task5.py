# **Task5: Contact Quick Lookup**
# - Store three names and their phone numbers in two separate tuples.
# - Create a dictionary from them using `dict(zip(...))`.
# - Ask the user for a name and display the corresponding number (or an error message).
# - Requirements:
# - Use `zip()` and d`ict()` to combine tuples.
# - Use `.get()` for safe retrieval.
# - No loops.

# Contact Quick Lookup

# Store three names and their phone numbers in two tuples
names = ("Alice", "Bob", "Charlie")
numbers = ("08012345678", "08087654321", "08011223344")

# Create a dictionary using zip() and dict()
contacts = dict(zip(names, numbers))

# Ask the user for a name
search_name = input("Enter a name to look up the phone number: ").strip()

# Display the corresponding number or an error message
result = contacts.get(search_name)
if result:
    print(f"{search_name}'s number is: {result}")
else:
    print("Name not found in contacts.")