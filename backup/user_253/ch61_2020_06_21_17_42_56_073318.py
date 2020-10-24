def filtra_positivos(lista):
    b=[]
    for item in range(len(lista)):
        if lista[item]>0:
            b.append(lista[item])
    return b
            