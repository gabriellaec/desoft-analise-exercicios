lista = []
i = 0
while lista[i] != 0:
    int(input('Diga o número? '))
    lista.append(lista[i])
    i = i + 1
print(sum(lista))