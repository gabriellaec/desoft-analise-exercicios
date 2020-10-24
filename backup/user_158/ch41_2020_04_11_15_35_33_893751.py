def zera_negativos(lista):
    i=0
    for i in range(0,len(lista)):
        if lista[i] < 0:
            lista[i]=0
    return lista