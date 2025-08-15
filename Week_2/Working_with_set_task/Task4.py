# Task4: 
# Create a Unique Voters Registration System
# - Ask for voter names and store in a set.
# - If a voter tries to register twice, display a warning.
# - After registration, display the total number of unique voters.

voters = set()
names = input("Please enter your name(s) to register as a voter (separate with commas): ")

for name in names.split(","):
    name = name.strip()
    if name in voters:
        print(f"Warning: {name} is already registered.")
    else:
        voters.add(name)
        print(f"{name} has been successfully registered.")

print(f"Total unique voters registered: {len(voters)}")
print(f"Registered voters: {sorted(voters)}")
