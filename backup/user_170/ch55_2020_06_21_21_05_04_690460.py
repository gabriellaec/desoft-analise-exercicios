def encontra_maximo(matriz):
    maximo = 0
    matriz = matriz[0]+matriz[2]+matriz[3]
    for i in range(len(matriz)):
        matriz[i] = abs(matriz[i])
    for i in matriz:
        if maximo < max(matriz[i]):
            maximo = max(matriz[i])
    return maximo