def filtra_positivos (lista):
    lista2 = []
    for i in range(len(lista)):
        if lista[i] > 0:
            lista2.append(lista[i])
    return lista2