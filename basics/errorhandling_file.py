fname = input("Enter the file name: ")
count = 0
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith('From:'):
            print(line)
            count = count + 1
except:
    print('File cannot be opened:', fname)
print('Line Count:', count)