def filtra_positivos(lista):
    lista2 = []
    i=0
    while i < len(lista):
        if lista[i] > 0:
            lista2.append(lista[i])
    return lista2

