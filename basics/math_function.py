import math

# Demonstrating the use of various math functions

# Square root
number = 16
sqrt_result = math.sqrt(number)
print(f"The square root of {number} is {sqrt_result}")

# Power
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}")

# Factorial
number = 5
factorial_result = math.factorial(number)
print(f"The factorial of {number} is {factorial_result}")

# Greatest Common Divisor (GCD)
num1 = 48
num2 = 18
gcd_result = math.gcd(num1, num2)
print(f"The greatest common divisor of {num1} and {num2} is {gcd_result}")

# Trigonometric functions
angle = math.pi / 4  # 45 degrees in radians
sin_result = math.sin(angle)
cos_result = math.cos(angle)
tan_result = math.tan(angle)
print(f"The sine of 45 degrees (π/4 radians) is {sin_result}")
print(f"The cosine of 45 degrees (π/4 radians) is {cos_result}")
print(f"The tangent of 45 degrees (π/4 radians) is {tan_result}")

# Logarithm
number = 100
log_result = math.log10(number)
print(f"The base-10 logarithm of {number} is {log_result}")

# Exponential
number = 2
exp_result = math.exp(number)
print(f"The exponential of {number} (e^{number}) is {exp_result}")

# Rounding functions
number = 3.14159
ceil_result = math.ceil(number)
floor_result = math.floor(number)
print(f"The ceiling of {number} is {ceil_result}")
print(f"The floor of {number} is {floor_result}")

import random

# Random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# Random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Random item from a list
items = ['apple', 'banana', 'cherry']
random_item = random.choice(items)
print(f"Random item from the list: {random_item}")

# Shuffle a list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"Shuffled list: {items}")

# Random sample of 3 items from a list
sample_items = random.sample(items, 3)
print(f"Random sample of 3 items from the list: {sample_items}")

# Random float between 1.0 and 10.0
random_uniform = random.uniform(1.0, 10.0)
print(f"Random float between 1.0 and 10.0: {random_uniform}")

# Random float from Gaussian distribution with mean 0 and std dev 1
random_gauss = random.gauss(0, 1)
print(f"Random float from Gaussian distribution with mean 0 and std dev 1: {random_gauss}")