def filtra_positivos (lista):
    lista1 = []
    for i in lista:
        if lista[i] > 0:
            lista1.append(lista[i])
    return lista1