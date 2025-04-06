import string

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File not found:", fname)
    exit()
counts = dict()
for line in fhand:
    line = line.strip()
    line = line.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    line = line.lower()  # Convert to lowercase
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)