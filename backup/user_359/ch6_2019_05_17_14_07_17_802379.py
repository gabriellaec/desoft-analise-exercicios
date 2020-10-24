def encontra_maximo(matriz):
    maximo = matriz[0][0]
    for row in matriz:
        for tile in row:
            if abs(tile) > abs(maximo):
                maximo = abs(tile)
    return maximo
            