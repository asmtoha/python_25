num_list = []
while (True):
    inp = input("Enter a number: ")
    if inp == 'done': break
    value = float(inp)
    num_list.append(value)
print(f"maximum: {max(num_list)}",f"minimum: {min(num_list)}")