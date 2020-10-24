def zera_negativos(lista):
    l = [-1, 4, 0, 24, -31, -1]
    i = 0
    if lista < 0:
        lista = 0
    return zera_negativos(l)