def zera_negativos(lista):
    i=0
    for i in lista:
        if lista[i] < 0:
            lista[i]=0
    return lista