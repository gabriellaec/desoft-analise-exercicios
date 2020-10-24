def zera_negativos(lista):
    for e in lista:
        if e < 0:
            e = 0
    return lista
    