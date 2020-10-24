def filtra_positivos(lista):
    positivos=[]
    i=0
    while i<len(lista):
        i+=1
        if lista[i]>=0:
            positivos.append(lista[i])
    return positivos 