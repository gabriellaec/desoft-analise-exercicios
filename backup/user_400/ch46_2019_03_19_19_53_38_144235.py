i = input()
c = 0
lista = []
lista2 = []
h = 0
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
while h < len(lista2):
    print(lista2[h])
    h += 1