def filtra_positivos(lista):
    novalista = []
    i = 0
    while i < len(lista):
        if lista[i]>=0:
            novalista.append(lista[i])
        i+=1
    return novalista