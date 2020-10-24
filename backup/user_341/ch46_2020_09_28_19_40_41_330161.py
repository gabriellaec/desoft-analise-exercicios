def numero_no_indice(lista):
    list = []
    i = 0
    while i < len(lista):
        if i == lista[i]:
            list.append(lista[i])
            i = i + 1
        else:
            i = i + 1

    return list
print(numero_no_indice([0, 5, 9, 3]))
