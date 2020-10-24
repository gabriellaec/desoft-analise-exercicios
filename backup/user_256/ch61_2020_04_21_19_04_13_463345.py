def filtra_positivos(lista):
    i = 0
    nova = []
    while i< len(lista):
        if lista[i]>0:
            nova.append(lista[i])
    return nova
        