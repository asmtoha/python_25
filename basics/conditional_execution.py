# Boolean expressions
print("Is 5 equal to 5?", 5 == 5)  # True
print("Is 5 equal to 6?", 5 == 6)  # False

# Not equal
print("Is 5 not equal to 6?", 5 != 6)  # True
print("Is 5 not equal to 5?", 5 != 5)  # False

# Greater than
print("Is 5 greater than 6?", 5 > 6)  # False
print("Is 5 greater than 4?", 5 > 4)  # True

# Less than
print("Is 5 less than 6?", 5 < 6)  # True
print("Is 5 less than 4?", 5 < 4)  # False

# Greater than or equal to
print("Is 5 greater than or equal to 5?", 5 >= 5)  # True
print("Is 5 greater than or equal to 6?", 5 >= 6)  # False

# Less than or equal to
print("Is 5 less than or equal to 5?", 5 <= 5)  # True
print("Is 5 less than or equal to 4?", 5 <= 4)  # False

# Logical operators
# And
print("True and True is", True and True)  # True
print("True and False is", True and False)  # False
print("False and False is", False and False)  # False

# Or
print("True or True is", True or True)  # True
print("True or False is", True or False)  # True
print("False or False is", False or False)  # False

# Not
print("Not True is", not True)  # False
print("Not False is", not False)  # True

# Membership operators
# In
print("Is 'H' in 'Hello'?", "H" in "Hello")  # True
print("Is 'h' in 'Hello'?", "h" in "Hello")  # False

# Not in
print("Is 'H' not in 'Hello'?", "H" not in "Hello")  # False
print("Is 'h' not in 'Hello'?", "h" not in "Hello")  # True

# Identity operators
# Is
x = 5
y = 5
print("Is x the same object as y?", x is y)  # True

# Is not
x = 5
y = 6
print("Is x not the same object as y?", x is not y)  # True

# Conditional statements
# If statement
x = 5
if x > 0:
    print("x is positive")

# If-else statement
x = -5
if x > 0:
    print("x is positive")
else:
    print("x is negative")

# If-elif-else statement
x = 0
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Nested if statement
x = 5
if x >= 0:
    if x == 0:
        print("x is zero")
    else:
        print("x is positive")
else:
    print("x is negative")

# Short hand if
x = 5
if x > 0: print("x is positive")

# Short hand if-else
x = -5
print("x is positive") if x > 0 else print("x is negative")

# Short hand if-elif-else
x = 0
print("x is positive") if x > 0 else print("x is zero") if x == 0 else print("x is negative")

# Pass statement
x = 5
if x > 0:
    pass
else:
    print("x is negative")

# Ternary operator
x = 5
print("x is positive") if x > 0 else print("x is negative")

# Multiple ternary operators
x = 0
print("x is positive") if x > 0 else print("x is zero") if x == 0 else print("x is negative")

# Nested ternary operators
x = 0
output = "x is positive" if x > 0 else "x is zero" if x == 0 else "x is negative"
print(output)

# Multiple conditions
x = 5
if x > 0 and x % 2 == 0:
    print("x is positive and even")
if x > 0 or x % 2 == 0:
    print("x is positive or even")

# Multiple conditions using ternary operator
x = 5
print("x is positive and even") if x > 0 and x % 2 == 0 else print("x is positive or even")

# Multiple conditions using nested ternary operator
x = 5
output = "x is positive and even" if x > 0 and x % 2 == 0 else "x is positive or even"
print(output)