def zera_negativos(lista):
    for item in range(len(lista)):
        if lista[item]< 0:
            item = 0
    return lista
    