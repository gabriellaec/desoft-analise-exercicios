def filtra_positivos(lista):
    for i in range(len(lista)):
        if len(lista)==0:
            break  
        if lista[i]<=0:
            del lista[i] 
    return lista                  