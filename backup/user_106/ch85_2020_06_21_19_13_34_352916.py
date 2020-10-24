numero = 0
file = open("macacos-me-mordam.txt", "r")
for line in file:
    for l in line.split():
        if l.upper() == "BANANA" or l.upper() == "BANANA.":
            numero += 1
print(numero)