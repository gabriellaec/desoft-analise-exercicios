import math
def encontra_maximo(matriz):
    lista0 = matriz[0]
    lista1 = matriz[1]
    lista2 = matriz[2]
    nm = lista0[0]
    i = 1
    while i < len(lista0):
        if math.abs(lista0[i]) > nm:
            nm = lista0[i]
        i = i + 1
    i = 0
    while i < len(lista1):
        if math.abs(lista1[i)] > nm:
            nm = lista1[i]
        i = i + 1
    i = 0
    while i < len(lista2):
        if math.abs(lista2[i]) > nm:
            nm = lista2[i]
        i = i + 1
    return nm