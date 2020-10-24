def filtra_positivos(numeros):
    i=0
    positivos=[]
    while i<len(numeros):
        if numeros[i]>0:
            positivos.append(numeros[i])
        i+=1
    return positivos