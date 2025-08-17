# Student Profile Builder

# 1. Collect basic info
name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter student's gender: ")

# 2. Academic scores for fixed subjects
subjects = ("Math", "English", "Science")
scores = tuple(float(input(f"Enter score for {subj}: ")) for subj in subjects)

# 3. Guardian info
guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

# 4. Hobbies (remove duplicates)
hobbies_input = input("Enter at least 3 hobbies (comma-separated): ")
hobbies_set = set(h.strip() for h in hobbies_input.split(","))

# 5. Build the student profile dictionary
student_profile = {
    "Basic Info": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.capitalize()
    },
    "Academics": {subj: score for subj, score in zip(subjects, scores)},
    "Guardian": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone
    },
    "Hobbies": list(hobbies_set)
}

# 6. Add calculated values
student_profile["Academics"]["Average"] = sum(scores) / len(scores)
student_profile["Basic Info"]["Initials"] = "".join([n[0].upper() for n in name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

# 7. Display results neatly
print("\n\t=== STUDENT PROFILE ===")
print(f"Name:\t\t{student_profile['Basic Info']['Name']}")
print(f"Age:\t\t{student_profile['Basic Info']['Age']}")
print(f"Gender:\t\t{student_profile['Basic Info']['Gender']}")
print(f"Initials:\t{student_profile['Basic Info']['Initials']}")

print("\n--- Academic Scores ---")
for subj, score in student_profile["Academics"].items():
    if subj != "Average":
        print(f"{subj}:\t\t{score}")
print(f"Average:\t{student_profile['Academics']['Average']:.2f}")

print("\n--- Guardian Info ---")
print(f"Name:\t\t{student_profile['Guardian']['Name']}")
print(f"Phone:\t\t{student_profile['Guardian']['Phone']}")

print("\n--- Hobbies ---")
print(", ".join(student_profile["Hobbies"]))
print(f"\nTotal Hobbies:\t{student_profile['Hobbies Count']}")