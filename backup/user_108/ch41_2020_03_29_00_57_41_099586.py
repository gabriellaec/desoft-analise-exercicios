def zera_negativos(lista):
    return list(map(lambda x: x if x>=0 else 0, lista))