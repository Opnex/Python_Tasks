# Days and Activities Pairing
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
activities = []

# Collect activities for the first three days
for day in days_of_week[:3]:
    activity = input(f"Enter an activity for {day}: ")
    activities.append(activity)

# Pair days and activities using dictionary comprehension and zip
day_activity_dict = {day: activity for day, activity in zip(days_of_week[:3], activities)}

# Output the dictionary
print("\nPaired Days and Activities:")
print(day_activity_dict)