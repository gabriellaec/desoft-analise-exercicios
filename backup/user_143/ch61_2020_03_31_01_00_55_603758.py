
def filtra_positivos (lista):
    i=0
    lista1=[]
    while i<len(lista):
        y=lista[i]
        while y>0:
            lista1.append(y)
            i+=1
        i+=1
    return lista1
                 
        