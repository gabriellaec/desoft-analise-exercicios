def encontra_maximo(matriz):
    maximo=0
    for row in matriz:
        for tile in row:
            if tile > maximo:
                maximo = tile
    return maximo
            