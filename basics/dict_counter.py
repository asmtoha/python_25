word = "I am nothing in this universe"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)