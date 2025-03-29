""" Write a program that reads the words in words.txt and stores them as
 keys in a dictionary. It doesn’t matter what the values are. Then you
 can use the in operator as a fast way to check whether a string is in the
 dictionary.
"""
fhand = open('words.txt')
word_dict = dict()

# Read each line, split into words, and store them as keys in the dictionary
for line in fhand:
    words = line.split()
    for word in words:
        word_dict[word] = True  # Value can be anything, e.g., True

# Print the dictionary (optional, for debugging)
print(word_dict)

# Example: Check if a word exists in the dictionary
search_word = input("Enter a word to check: ")
if search_word in word_dict:
    print(f"'{search_word}' is in the dictionary.")
else:
    print(f"'{search_word}' is NOT in the dictionary.")