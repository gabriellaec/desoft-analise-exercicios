def filtra_positivos(lista):
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]>0:
            lista1.append(lista[i])
        i+=1
    return lista1