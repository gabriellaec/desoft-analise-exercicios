def zera_negativos (lista):
    j=len(lista)
    i=0
    while i<j:
        if lista[i]<0:
            lista[i]=lista[i]*(-1)
        else:
            lista[i]=lista[i]
        i+=1
    return lista