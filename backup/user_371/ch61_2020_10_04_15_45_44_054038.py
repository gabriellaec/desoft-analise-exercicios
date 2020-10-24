def filta_positivos(lista):
    i=0
    lista_nova=[]
    while len(lista)>i:
        if lista[i]<0:
            i+=1
        else:
            lista_nova.append(lista[i])
            i+=1
    return lista_nova