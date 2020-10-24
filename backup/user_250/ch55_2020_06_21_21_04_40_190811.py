def encontra_maximo(matriz):
    lista = []
    for i in matriz:
        for i2 in i:
            lista.append(abs((i2)))
    return max(lista)