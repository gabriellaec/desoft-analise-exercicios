def filtra_positivos (lista):
    i = 0
    lista2 = []
    while lista[i] > 0:
        lista2.append(lista[i])
        i += 1
    return lista2  