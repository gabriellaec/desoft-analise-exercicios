def filtra_positivos(lista):
    for i in range(len(lista)):
        if lista[i]<=0:
            del lista[i]
        if len(lista)==0:
             break   
    return lista                  