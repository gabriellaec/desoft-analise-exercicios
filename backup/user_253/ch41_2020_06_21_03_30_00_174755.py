def zera_negativos(lista):
    for item in lista:
        if lista[item]< 0:
            item = 0
    return lista
    