""" Exercise 4: Download a copy of the filewww.py4e.com/code3/romeo.txt.
 Write a program to open the file romeo.txt and read it line by line. For
 each line, split the line into a list of words using the split function.
 For each word, check to see if the word is already in a list. If the word
 is not in the list, add it to the list. When the program"""
fhand = open('romeo.txt')
word_list = list()
for line in fhand:
    line = line.strip()
    print(line)
    words = line.split()
    print(words)
    for word in words:
        if word not in word_list:
            word_list.append(word)
print(sorted(word_list))