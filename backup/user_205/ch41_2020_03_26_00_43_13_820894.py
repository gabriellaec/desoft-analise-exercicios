def zera_negativos(lista):
    for i in range(lista):
        if lista[i]<0:
            lista[i]=0
    return lista