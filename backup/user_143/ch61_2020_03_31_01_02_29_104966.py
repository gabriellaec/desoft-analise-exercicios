def filtra_positivos (lista):
    i=0
    lista1=[]
    while i<len(lista):
        y=lista[i]
        if y>0:
            lista1.append(y)
            i+=1
        else:
            i+=1
    return lista1
                 
        