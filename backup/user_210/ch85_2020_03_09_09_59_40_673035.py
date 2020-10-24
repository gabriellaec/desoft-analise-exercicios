cont = 0
with open(r"macacos-me-mordam.txt", "r") as lines:
    for c in lines:
        if c.upper() == "BANANA":
            cont += 1
print(cont)