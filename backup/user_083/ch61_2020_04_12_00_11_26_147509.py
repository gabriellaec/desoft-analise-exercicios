def filtra_positivos(lista):
    lista=[0,1,2,3,-4]
    for i in range(len(lista)):
        if lista[i]<=0:
            del lista[i]
        return lista
                    