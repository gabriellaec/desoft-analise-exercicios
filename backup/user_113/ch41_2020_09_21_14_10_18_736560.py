def zera_negativos(lista):
    x=0
    while x < len(lista):
        if lista[x]<0:
            lista[x] = 0
        x += 1
    return lista