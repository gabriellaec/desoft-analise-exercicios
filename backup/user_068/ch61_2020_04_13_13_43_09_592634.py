def filtra_positivos(lista):
    i = 0
    novalista =[]
    while i < len(lista):
        if lista[i] >= 0:
            novalista.append(lista[i])
        i += 1
    return b