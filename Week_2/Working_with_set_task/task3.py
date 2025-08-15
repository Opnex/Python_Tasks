# Task3: 
# Simulate a football match ticket system
# - Store all seat numbers (1 to 50) in a set
# - Ask users to "book" a seat by entering the number.
# - Remove booked seats from the set.
# - Show remaining seats after each booking.

seat_number = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
print(f"Available seats: {sorted(seat_number)}")
book_seat = input("Please enter your seat number: ")
seat_number.remove(int(book_seat))
print(f"Your seat number {book_seat} has been booked successfully.")
print(f"Available seats: {sorted(seat_number)}")
