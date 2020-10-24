def encontra_maximo(matriz):
    max=matriz[0][0]
    for i in range(3):
        for j in range(3):
            if matriz[i][j]>max:
                max=matriz[i][j]
    return max