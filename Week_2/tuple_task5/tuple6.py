days_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
months_year = ("January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December")

student_name = input("Please enter your name: ")
gender = input("Enter your gender: ")
course = input("What's your course: ")

# Get current month number from user (1 to 12)
month = int(input("Enter current month in number (1-12): "))

# Get current day number from user (1 to 7)
day = int(input("Enter today's day number (1-7): "))

# Display details
print("Student Name:", student_name)
print("Gender:", gender)
print("Course:", course)
print("Month:", months_year[month - 1])  # Subtract 1 because index starts at 0
print("Day:", days_week[day - 1])
