def zera_negativos(lista):
    a= lista
    i=0
    while i<len(lista):
        if lista[i]<0:
            lista[i]=0
            i+=1
    else:
        i+=1
    return a
        
