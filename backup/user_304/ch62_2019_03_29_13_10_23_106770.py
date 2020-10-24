def filtra_positivos(lista):
    positivos=[]
    i=0
    while i<len(lista):
        if lista[i]>=0:
            positivos.append(lista[i])
        i+=1
    return positivos 