fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
        count = count + 1
print('Line Count:', count)