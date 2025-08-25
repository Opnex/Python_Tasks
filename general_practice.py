story = '''Once upon a time 
opnex used to  be a small boy
but now he has grown up
and one day he will become a great programmer'''
print(story)


name = "Opnex "
age = 20
gender = "male"
school = "BCA"
course = "bed"
# print(name + " " + str(age) + " " + gender + " " + school + " " + course)
print(f"{name * 5} {age * 5}")
print(age * 5)

sentence = "Opnex is a good programmer"
print("programmer" in sentence)
print("opeyemi" in sentence)
print("Opnex" not in sentence)

print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())
print(sentence.replace("good", "great"))
print(sentence.split())
print(sentence.split(" "))
print(sentence.strip())
print(sentence.swapcase())
print(" ".join(name))