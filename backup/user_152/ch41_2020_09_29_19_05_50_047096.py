def zera_negativos (lista):
    i = 0
    size = len(lista)
    while i<size:
        if lista[i] < 0:
            lista[i] = 0
    return lista