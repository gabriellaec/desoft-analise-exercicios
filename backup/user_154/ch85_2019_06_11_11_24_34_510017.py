total = 0

with open("macacos-me-mordam.txt", "r") as file:
   for line in file.readlines():
      splt = line.split("banana")
      total = total + len(splt)
print(total)    