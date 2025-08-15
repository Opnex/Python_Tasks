# Upper()
# Converts all characters in the string to uppercase.

name = "Ada Balogun"
print(name.upper())   # Output: ADA BALOGUN


# Lower()
# Converts all characters in the string to lowercase.
sentence = "Python Is Amazing"
print(sentence.lower()) # Output: python is amazing


# Strip()
# Removes whitespace (or specified characters) from both ends of the string.

text = "  Abuja  "
print(text.strip())  # Output: Abuja


# replace()
# Replaces occurrences of a substring with another substring.
message = "I love Java"
print(message.replace("Java", "Python")) # Output: I love Python


# Swapcase()
# Switches lowercase to uppercase and vice versa.
text = "hello ABEOKUTA"
print(text.swapcase()) # Output: hELLO abeokuta


# lstrip()
# Removes whitespace (or specified characters) from the left side only.
text = " Nigeria"
print(text.lstrip()) # Output: Nigeria

# rstrip()
# Removes whitespace (or specified characters) from the right side only.
text = "Nigeria "
print(text.rstrip()) # Output: Nigeria



# Split()
# Splits a string into a list using a separator (default is space).
fruits = "mango orange banana"
print(fruits.split()) # Output: ['mango', 'orange', 'banana']


# rsplit()
# Splits a string into a list from the right side.
text = "one,two,three,four"
print(text.rsplit(",", 2)) # Output: ['one,two', 'three', 'four']



# Splitlines()
# Splits a string into a list at each newline (\n).
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())  # Output: ['Line 1', 'Line 2', 'Line 3']


# join()
# Joins a list of strings into one string with a specified separator.
words = ["I", "love", "Python"]
print(" ".join(words)) # Output: I love Python


# center()
# Centers the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.center(20, "_")) # Output: -------Python-------


# ljust()
# Left-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.ljust(10, "*")) # Output: Python****


# rjust()
# Right-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.rjust(10, "*"))  # Output: ****Python


# zfill()
# Pads a numeric string on the left with zeros until it reaches a given length.
num = "42"
print(num.zfill(5))  # Output: 00042


# isalpha()
# Checks if the string contains only letters.
print("Lagos".isalpha())  # True
print("Lagos123".isalpha())  # False


# isdigit()
# Checks if the string contains only digits.
print("12345".isdigit())  # True
print("123a".isdigit())   # False


# isalnum()
# Checks if the string contains only letters and digits.
print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False