counts = {'Toha':1,"Ali":2,"Sami":3,"Tariq":4}
print(counts.get("Toha",0)) # 1
print(counts.get("Ali",0)) # 2
print(counts.get("Sam",0)) # WHEN NOT FOUND 0