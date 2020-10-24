cont = 0
for c in open(r"macacos-me-mordam.txt", "r").read():
    if c.upper() == "BANANA":
        cont += 1
print(cont)