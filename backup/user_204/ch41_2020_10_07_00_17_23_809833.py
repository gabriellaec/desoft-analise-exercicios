def zera_negativos(lista1):
    tam = len(lista1)
    i = 0
    while i < tam:
        if lista1[i] < 0:
            lista1[i] = 0
        i = i + 1