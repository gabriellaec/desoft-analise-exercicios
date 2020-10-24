i = input()
c = 0
t = 0
lista = []
lista2 = []
while i != "fim":
    lista.append(i)
    i = input()
lista.append(i)
while c < len(lista):
    g = lista[c]
    if g[t] == "a":
        lista2.append(g)
        c += 1
    else:
        c += 1
