# Ask for first three items
item1 = input("Please your first item: ")
item2 = input("Please your second item: ")
item3 = input("Please your third item: ")

# Store in tuple
shopping_list = (item1, item2, item3)

# Convert to list
items = list(shopping_list)

# Ask for two more items
item4 = input("Add another item: ")
item5 = input("Add another item: ")

# Add them to the list
items.append(item4)
items.append(item5)

# Convert back to tuple
shopping_lists = tuple(items)

# Display with " | " separator
print("Your shopping list:", " | ".join(shopping_lists))
