total = 0
for i in open("churras.txt", "r").readlines():
    lista = str(i).split(",")
    total += float(lista[1])*float(lista[2])
print(total)