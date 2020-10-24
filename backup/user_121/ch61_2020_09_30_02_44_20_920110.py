def filtra_positivos(lista):
    lista_nova=[]
    i=0
    while i<len(lista):
        if lista[i]>0:
            lista_nova.append(lista[i])
        i+=1
    return lista_nova