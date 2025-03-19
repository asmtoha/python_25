# Basic Exception Handling
try:
    # Attempt to divide by zero
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the division by zero error
    print("Error: Division by zero is not allowed. Please check your divisor.")

# Handling Multiple Exceptions
try:
    # Attempt to convert a string to an integer
    value = int("abc")
except ValueError as e:
    # Handle the value error
    print("Error: Cannot convert 'abc' to an integer. Please provide a valid number.")
except TypeError as e:
    # Handle the type error
    print("Error: Type error occurred. Please check the data types.")

# Using else and finally
print("else-finally\n")
try:
    # Attempt a valid division
    result = 10 / 2
except ZeroDivisionError as e:
    # Handle the division by zero error
    print("Error: Division by zero is not allowed. Please check your divisor.")
else:
    # This block runs if no exception occurs
    print("Division successful, the result is:", result)
finally:
    # This block always runs
    print("This block always executes, regardless of an exception.")

# Raising Exceptions
try:
    age = -1
    if age < 0:
        # Manually raise a ValueError
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    # Handle the manually raised ValueError
    print("Error:", e)

# Custom Exceptions
class NegativeAgeError(Exception):
    pass

try:
    age = -1
    if age < 0:
        # Manually raise a custom exception
        raise NegativeAgeError("Age cannot be negative.")
except NegativeAgeError as e:
    # Handle the custom exception
    print("Error:", e)

# Catching All Exceptions
try:
    # Attempt to divide by zero
    result = 10 / 0
except Exception as e:
    # Handle any type of exception
    print("An error occurred:", e)

# Nested Exception Handling
try:
    try:
        # Attempt to divide by zero
        result = 10 / 0
    except ZeroDivisionError as e:
        # Handle the division by zero error and re-raise it
        print("Inner error: Division by zero.")
        raise
except Exception as e:
    # Handle the re-raised exception
    print("Outer error:", e)