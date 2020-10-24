lista = []
a = input("Digite alguma coisa legal: ")
while a != "fim":
    lista.append(a)
    a = input("Digite alguma coisa legal: ")
b = len(lista)
del lista[b]

nova_lista = []
i = 0
while i < len(lista):
    if lista[i][0] == "a":
        nova_lista.append(lista[i])
    i += 1
return nova_lista