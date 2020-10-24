def filtra_positivos(lista):
    for i in range(len(lista+1)):
        if (lista[i]<0):
            del lista[i]
    return lista