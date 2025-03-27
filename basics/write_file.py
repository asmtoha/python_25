fout = open('output.txt', 'w')
about_me = "Hi, I am A. S. M. Toha. I am trying to learn"
fout.write(about_me)
fout.close()

fhand = open('output.txt')
print(fhand.read())