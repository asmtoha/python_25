#string concatenation
a = "Hello"
b = "World"
# Concatenation
concat = a + b  # HelloWorld
print("Concatenation:",concat)
#string repetition
repetition = a * 3  # HelloHelloHello
print("Repetition:",repetition)
#string slicing
string = "Hello, World!"
slice = string[3:8]  # lo, W
print("Slicing:",slice)
#string length
length = len(string)  # 13
print("Length:",length)

#string methods
#lower() method returns the string in lowercase.
print("Lowercase:",string.lower())
#upper() method returns the string in uppercase.
print("Uppercase:",string.upper())
#capiatalize the first letter of the string.
capitalize = string.capitalize()  # Hello, world!
print("Capitalize:",capitalize)
#title() method returns the string in title case.
title = string.title()  # Hello, World!
print("Title:",title)
#count() method returns the number of occurrences of a substring in the given string.
count = string.count("l")  # 3
print("Count:",count)
#find() method returns the index of the first occurrence of a substring.
find = string.find("World")  # 7
print("Find:",find)
#replace() method replaces a substring with another substring.
replace = string.replace("World", "Python")  # Hello, Python!
print("Replace:",replace)
#split() method splits the string based on the specified separator.
split = string.split(",")  # ['Hello', ' World!']
print("Split:",split)
#strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
strip = string.strip()  # Hello, World!
print("Strip:",strip)
#join() method joins the elements of an iterable to the end of the string.
join = "-".join(["Hello", "World"])  # Hello-World
print("Join:",join)
#startswith() method returns True if the string starts with the specified substring.
startswith = string.startswith("Hello")  # True
print("Startswith:",startswith)
#endswith() method returns True if the string ends with the specified substring.
endswith = string.endswith("World!")  # True
print("Endswith:",endswith)
#isalnum() method returns True if all characters in the string are alphanumeric.
isalnum = string.isalnum()  # False
print("Isalnum:",isalnum)
#isalpha() method returns True if all characters in the string are alphabets.
isalpha = string.isalpha()  # False
print("Isalpha:",isalpha)
#isdigit() method returns True if all characters in the string are digits.
isdigit = string.isdigit()  # False
print("Isdigit:",isdigit)

#string formatting
# Using the % operator
name = "Alice"
age = 10
# %s is used as a placeholder for string values you want to inject into the string.
# %d is used as a placeholder for numeric or decimal values.
# %f is used as a placeholder for float values.
formatted_string = "Hello, %s. You are %d." % (name, age)
print("Using % Operator:",formatted_string)
# Using the format() method
name = "Alice"
age = 10
# {} is used as a placeholder for string values you want to inject into the string.
formatted_string = "Hello, {}. You are {}.".format(name, age)
print("Using format() Method:",formatted_string)
# Using f-string
name = "Alice"
age = 10
# f-string starts with f and is prefixed before the string.
formatted_string = f"Hello, {name}. You are {age}."
print("Using f-string:",formatted_string)
# Using Template Strings
from string import Template
name = "Alice"
age = 10
# $name and $age are placeholders for string values you want to inject into the string.
template = Template("Hello, $name. You are $age.")
formatted_string = template.substitute(name=name, age=age)
print("Using Template Strings:",formatted_string)
# Using the + operator
name = "Alice"
age = 10
# + operator concatenates the string with the variables.
formatted_string = "Hello, " + name + ". You are " + str(age) + "."
print("Using + Operator:",formatted_string)
