numero = 0
file = open("macacos-me-mordam.txt", "r")
lines = file.readlines()
for line in lines:
    line = line.strip()
    for l in line.split():
        if l.upper() == "BANANA" or l.upper() == "BANANA.":
            numero += 1
print(numero)