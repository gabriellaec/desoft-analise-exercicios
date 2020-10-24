
def filtra_positivos(lista):
    c = []
    for i in range(len(lista)):
        if (lista[i]>0):
            c.append(lista[i])
    return c