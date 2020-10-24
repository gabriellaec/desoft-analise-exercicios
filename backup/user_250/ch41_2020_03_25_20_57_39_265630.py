def zera_negativos(lista):
    n=0
    while n < len(lista):
        if lista[n]<0:
            lista[n]=0
        n=n+1
    return(lista)