# For loop example
print("For loop example:")
for i in range(5):
    print(f"Current value of i: {i}")
print("For loop ended.\n")

# While loop example
print("While loop example:")
i = 0
while i < 5:
    print(f"Current value of i: {i}")
    i += 1
print("While loop ended.\n")

# For loop with break example
print("For loop with break example:")
for i in range(10):
    if i == 5:
        print("Breaking the loop as i equals 5")
        break
    print(f"Current value of i: {i}")
print("For loop with break ended.\n")

# While loop with break example
print("While loop with break example:")
i = 0
while i < 10:
    if i == 5:
        print("Breaking the loop as i equals 5")
        break
    print(f"Current value of i: {i}")
    i += 1
print("While loop with break ended.\n")

# For loop with continue example
print("For loop with continue example:")
for i in range(10):
    if i % 2 == 0:
        print(f"Skipping the even number: {i}")
        continue
    print(f"Current value of i: {i}")
print("For loop with continue ended.\n")

# While loop with continue example
print("While loop with continue example:")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        print(f"Skipping the even number: {i}")
        continue
    print(f"Current value of i: {i}")
print("While loop with continue ended.\n")

# Nested for loop example
print("Nested for loop example:")
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")
print("Nested for loop ended.\n")

# Nested while loop example
print("Nested while loop example:")
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1
print("Nested while loop ended.\n")