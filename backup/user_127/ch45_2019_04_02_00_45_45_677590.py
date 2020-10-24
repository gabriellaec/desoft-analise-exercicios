def zera_negativos(lista):
    i=0
    n=len(lista)
    while i<n:
        while lista[i]<0:
            lista[i]=0
        i+=1
    return lista