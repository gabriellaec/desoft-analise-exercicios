positivos=[]
def filtra_positivos(lista):
    for i in range(len(lista)):
        if i>0:
            positivos.append(i)
    return positivos