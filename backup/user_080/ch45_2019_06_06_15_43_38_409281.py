def zera_negativos(lista):
    i=0
    while lista[i]>=0:
        if lista[i]<0:
            lista[i]=0
            i+=1
        else:
            i+=1
    return lista
        
    