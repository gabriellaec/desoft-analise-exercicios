def encontra_maximo (matriz):
    for i in range (0,4):
        max_linha =[]
        max_linha.append(max(matriz[i]))
    norma_infinita = max(max_linha)
    return norma_infinita