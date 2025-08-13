item1 = input("Please your first item: "),
item2 = input("Please your second item: "),
item3 = input("Please your third item: ")
shopping_lists = (item1, item2, item3)
items = list(shopping_lists)

item4 = input("add more"),
item5 = input("add more")
shopping_lists2 = item4, item5
final = tuple(shopping_lists)
print(shopping_lists.join("{final}"))

