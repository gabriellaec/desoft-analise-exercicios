def zera_negativos(lista):
    for a in lista:
        if a < 0:
            lista[lista.index(a)] = 0
    return lista