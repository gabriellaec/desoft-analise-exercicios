def filtra_positivos(lista):
    i=0
    t=0
    n=[]
    while i<len(lista):
        if lista[i]>=0:
            n.append(lista[i])
            t+=1
        i+=1
    return n
