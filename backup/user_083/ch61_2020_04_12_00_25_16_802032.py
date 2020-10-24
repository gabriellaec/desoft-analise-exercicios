def filtra_positivos(lista):
    lista=[]
    for i in range (len(lista)):
        if lista[i]>0:
            lista.append(i)
        else:
            del lista[i]
        return lista                  