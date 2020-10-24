def filtra_positivos (lista):
    for i in range(len(lista)):
        if lista[i] <= 0:
            lista.remove(lista[i])
    return lista