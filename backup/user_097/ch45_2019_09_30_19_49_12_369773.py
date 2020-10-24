def zera_negativos(lista):
    i = 0
    while (i<len(lista)):
        if(lista[i]<0):
            lista[i]=0
        i = i + 1
    return lista

l = [1, 2, 3, -4, -5, -6]

print(zera_negativos(l))