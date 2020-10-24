def filtra_positivos(lista):
    novalista=[]
    for i in range(len(lista)):
        if lista[i]>0:
            novalista.append(lista[i])