def filtra_positivos(lista):
    i = 0
    while i < len(lista):
        if lista[i] < 1:
            del lista[i]
        i += 1
    return lista
    