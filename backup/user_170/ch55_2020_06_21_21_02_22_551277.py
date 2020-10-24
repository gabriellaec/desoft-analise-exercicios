def encontra_maximo(matriz):
    maximo = 0
    matriz = abs(matriz)
    for i in matriz:
        if maximo < max(matriz[i]):
            maximo = max(matriz[i])
    return maximo