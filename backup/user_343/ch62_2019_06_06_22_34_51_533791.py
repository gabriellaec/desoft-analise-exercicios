def filtra_positivos(lista):
    positivo=[]
    i=0
    while i < len(lista):
        if lista[i]>0:
            positivo.append(lista[i])
            i+=1
    return positivo
    