i = input()
c = 0
lista = []
lista2 = []
while i != "fim":
    lista.append(i)
    i = input()
while c < len(lista):
    g = lista[c]
    if g[0] == "a":
        lista2.append(g)
        c += 1
    else:
        c += 1
print(lista2)