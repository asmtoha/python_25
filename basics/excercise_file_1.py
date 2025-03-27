# Write a program to read through a file and print the contents
#  of the file (line by line) all in upper case
fhand = input("Enter the file name: ")
try:
    fhand = open(fhand)
    for line in fhand:
        print(line.upper())
    
except:
    print('File cannot be opened:', fhand)
