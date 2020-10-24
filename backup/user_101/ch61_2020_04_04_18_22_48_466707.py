def filtra_positivos(lista):
    for e in lista:
        i = 0
        if lista[i] < 0:
            del lista[i]
        i += 1
    return lista