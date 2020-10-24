def filtra_positivos(lista):
    i=0
    while i<len(lista):
        if lista[i]>0:
            listaa.append(lista[i])
            i+=1
        else:
            i+=1
    return listaa