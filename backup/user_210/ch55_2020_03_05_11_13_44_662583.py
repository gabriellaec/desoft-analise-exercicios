def encontra_maximo(matriz):
    maximo = matriz[0][0]
    for c in matriz:
        if maximo < max(c):
            maximo = max(c)
    return maximo