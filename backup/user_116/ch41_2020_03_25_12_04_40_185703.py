def zera_negativos(lista):
    i=0
    num=len(lista)
    while i<num:
        if lista[i]<0:
            lista[i]=0
        i+=1
    return lista
