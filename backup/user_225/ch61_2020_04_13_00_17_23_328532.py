def filtra_positivos(lista):
    novalista = []
    for i in lista:
        if lista[i]==0:
            novalista.append(lista[i])
        elif lista[i]>0:
            novalista.append(lista[i])
    return novalista