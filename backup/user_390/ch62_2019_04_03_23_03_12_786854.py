
def filtra_positivos(lista):
    i=0
    listanova=[]
    while i<len(lista):
        if lista[i]>0:
            listanova.append(lista[i])
            i+=1
        else:
            i+=1
    return listanova
