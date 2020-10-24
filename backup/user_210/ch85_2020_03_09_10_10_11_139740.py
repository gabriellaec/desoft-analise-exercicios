cont = 0
with open("macacos-me-mordam.txt", "r") as file:
    for line in file:
        if line.strip().upper() == "BANANA":
            cont += 1
print(cont)