def filtra_positivos(lista):
    lista_nova=[]
    n=len(lista)
    for i in range(0,n):
        if lista[i]>0:
            lista_nova.append(lista[i])
    return lista_nova