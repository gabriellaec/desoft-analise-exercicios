def zera_negativos(lista1):
    i=0
    while i<len(lista1):
        if lista1[i]<0:
            lista1[i]=0
        i+=1
    retunr lista1