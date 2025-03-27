num_list = []
while (True):
    inp = input("Enter a number: ")
    if inp == 'done': break
    value = float(inp)
    num_list.append(value)
avg_of_list = sum(num_list)/len(num_list)
print('Average:', avg_of_list)