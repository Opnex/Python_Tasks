# Single quotes
name = 'Ada'
print(name)

#Double quotes
greetings = "Hello"
print(greetings)

# Triple quotes (for nmulti-line strings)
story = '''Once upon a time,
there was a coder named Ada'''
print(story)

# String with numbers and symbols 
password = "p@sswOrd123"
print(password) 



#Indexing
word = "Python"
print(word[0]) # print p
print(word[-1]) # print n



# Slicing
word = "Pythonings"
print(word[0:4])
print(word[2:])
print(word[:3])
print(word[::2])
print(word[::-1])


# Concatenation
a = "Hello"
b = "World"
print(a + " " + b) #Hello World


# Repetition
word = "Hi!"
print(word * 3) #Hi! Hi! Hi!


# Membership
text = "Python programming"
print("Python" in text) # True
print("Java" in text) # False
print("Java" not in text) # True


# find() / rfind()
text = "Hello World"
print(text.find("o"))
print(text.rfind("o"))


# Index() / rindex()
text = "Hello World"
print(text.index("World")) # 6


#`startswith() / endswith()`
filename = "data.csv"
print(filename.startswith("data")) # True
print(filename.endswith(".csv")) # True