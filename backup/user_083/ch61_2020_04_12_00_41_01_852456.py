def filtra_positivos(lista):
    i=0
    while i<(len(lista)):
        if len(lista)==0:
            break  
        if lista[i]<=0:
            del lista[i]
        i+=1
    return lista                  