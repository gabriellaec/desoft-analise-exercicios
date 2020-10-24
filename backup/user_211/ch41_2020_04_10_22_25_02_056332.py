def zera_negativos(x):
    lista=list(x)
    print(lista)
    for i in range(0,len(lista)):
        if lista[i]<0:
            lista[i]=0
    return lista