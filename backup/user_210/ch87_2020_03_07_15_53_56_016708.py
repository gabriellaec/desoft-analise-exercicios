total = 0
for c in open("churras.txt", "r").readlines():
    lista = str(c).split(",")
    total += lista[1]*lista[2]
print(total)