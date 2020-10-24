def filtra_positivos(lista):
    lista_nova=[]
    i=0
    n=len(lista)
    for i in range(n-1):
        if lista[i]>0:
            lista_nova.append(lista[i])
    return lista_nova