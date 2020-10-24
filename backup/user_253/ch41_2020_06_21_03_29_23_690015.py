def zera_negativos(lista):
    for item in lista:
        if lista[item]< 0:
            lista[item] = 0
    return lista
    