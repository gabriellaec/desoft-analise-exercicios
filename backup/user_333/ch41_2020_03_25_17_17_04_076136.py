def zera_negativos(lista):
    n=len(lista)-1
    while n>=0:
        if lista[n]<0:
            lista[n]=0
        n-=1
    return lista