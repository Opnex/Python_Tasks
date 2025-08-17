# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.
# - Convert them to a set to ensure uniqueness.
# - Create a dictionary where each name is a key and its length is the value.
# - Requirements
# - Use `.split(",")` and `set()` to remove duplicates.
# - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.

# Unique Members Registration

# Ask the user to enter three names separated by commas
names_input = input("Enter three names separated by commas: ")

# Convert to set to ensure uniqueness
set_of_names = set(name.strip() for name in names_input.split(","))

# Create dictionary: name as key, length as value
name_length_dict = {name: len(name) for name in set_of_names}

# Output the result
print("\nUnique names and their lengths:")
print(name_length_dict)