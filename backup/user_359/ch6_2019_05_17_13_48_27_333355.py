def encontra_maximo(matriz):
    
    for row in matriz:
        for tile in row:
            maximo = tile
            if tile > maximo:
                maximo = tile
    return maximo
            