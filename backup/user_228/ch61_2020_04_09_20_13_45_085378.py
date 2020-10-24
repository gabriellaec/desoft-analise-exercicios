def filtra_positivos(lista):
    i=0
    lista2=[]
    while i<len(lista):
        if lista[i]>0:
            i=i+1
            lista2.append(lista[i])
        else:
            i=i+1
            
    return lista2