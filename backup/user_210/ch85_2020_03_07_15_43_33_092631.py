cont = 0
for c in open("macacos-me-mordam.txt", "r"):
    if c.upper() == "BANANA":
        cont += 1
print(cont)