def filtra_positivos(lista):
    nova = []
    for i in lista:
        if lista[i] >= 0:
            lista.append(lista[i])
    return nova
    