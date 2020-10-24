def filtra_positivos (lista):
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[i] > 0:
            lista2.append(lista)
        else:
            i += 1
    return lista2