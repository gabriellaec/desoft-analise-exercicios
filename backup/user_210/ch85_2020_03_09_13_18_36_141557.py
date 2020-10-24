cont = 0
file = open("macacos-me-mordam.txt", "r")
#lines = file.readlines()
for line in file:
    line = line.strip()
    if line.upper() == "BANANA":
        cont += 1
print(cont)