def filtra_positivos(lista):
    nova = []
    for i in lista:
        if i > 0:
            nova.append(i)
    return nova