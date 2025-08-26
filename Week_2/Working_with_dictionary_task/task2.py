# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.
# - Items should come from a list.
# - Prices are entered by the user.
# - Display all items and prices, then allow the user to update the price of an item.
# - Requirements:
# - Use dictionary update method `.update()` or assignment.
# - Use `.keys()` to display available items.
# - Use input validation (no advanced functions).

# Super Market Price List
supermarket = {}
# Collect items from the user
items = input("Enter items (comma-separated): ")
item_list = [item.strip() for item in items.split(",")]
# Collect prices for each item
for item in item_list:
    price = float(input(f"Enter price for {item}: "))
    supermarket[item] = price
# ...existing code...

# Display all items and prices
print("\nSupermarket Price List:")
for item, price in supermarket.items():
    print(f"{item}: ₦{price:.2f}")

# Show available items
print("\nAvailable items:", ', '.join(supermarket.keys()))

# Update the price of an item
item_to_update = input("Enter the name of the item you want to update the price for: ").strip()
if item_to_update in supermarket:
    try:
        new_price = float(input(f"Enter new price for {item_to_update}: "))
        supermarket.update({item_to_update: new_price})
        print(f"Updated {item_to_update} to ₦{new_price:.2f}")
    except ValueError:
        print("Invalid price entered.")
else:
    print("Item not found in the list.")

# Display updated price list
print("\nUpdated Supermarket Price List:")
for item, price in supermarket.items():
    print(f"{item}: ₦{price:.2f}")