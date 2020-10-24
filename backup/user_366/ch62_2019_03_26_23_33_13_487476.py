def filtra_positivos(lista):
    i = 0
    while lista[i] < 0 and i < len(lista):
        del lista[i]
        i += 1
    return lista