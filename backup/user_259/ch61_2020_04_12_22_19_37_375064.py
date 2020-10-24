def filtra_positivos(lista):
    i = 0
    positivos = []
    while i<len(lista):
        if lista[i]>0:
            positivos.append(lista[i])
        else:
            i+=1
    return positivos

            