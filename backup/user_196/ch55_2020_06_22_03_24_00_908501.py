def encontra_maximo(matriz):
    valorabs = 0
    for i in range (len(matriz)):
        for c in range (matriz[i]):
            if matriz[i][c] > matriz[i-1][c-1]:
                valorabs = matriz[i][c]
    return valorabs