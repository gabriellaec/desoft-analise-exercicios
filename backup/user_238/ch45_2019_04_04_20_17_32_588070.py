def zera_negativos(lista):
    i=0
    while i< len(lista):
        if lista[i]<0:
            lista[i]=0
        i+=1
    return lista
lista=[1,2,3,-1,-4,8]
print(zera_negativos(lista))