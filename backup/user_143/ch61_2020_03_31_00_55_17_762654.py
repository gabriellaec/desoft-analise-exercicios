def filtra_positivos (lista):
    i=0
    lista1=[]
    while lista[i]>0 and i<len(lista):
        lista1.append(lista[i])
        i+=1
    i+=1
    return lista1
                 
        