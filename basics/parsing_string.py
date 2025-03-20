data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
start = data.find("@")
print("Find start:",start)

end = data.find(" ", start)
print("Find end:",end)

host = data[start+1 : end]
print("Host:",host)