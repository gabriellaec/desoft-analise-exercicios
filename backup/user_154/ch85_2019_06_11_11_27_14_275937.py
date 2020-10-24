total = 0

with open("macacos-me-mordam.txt", "r") as file:
   for line in file.readlines():
      splt = line.lower().split("banana")
      total = total + (len(splt) -1)
print(total)