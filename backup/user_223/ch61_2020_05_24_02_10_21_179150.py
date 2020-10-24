def filtra_positivos(lista):
    i=0
    while i < (len(lista)-1):
        if lista[i] <= 0:
            del lista[i]
    return lista