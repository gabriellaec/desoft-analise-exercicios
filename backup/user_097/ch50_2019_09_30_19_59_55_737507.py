def numero_no_indice(lista):
    i = 0
    listaIndices = []
    while (i<len(lista)):
        if(lista[i]==i):
            listaIndices.append(lista[i])
        i = i + 1
    return listaIndices

l = [0, 10, 2, 30, 4]

print(numero_no_indice(l))