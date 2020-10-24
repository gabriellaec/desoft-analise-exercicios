def calcula_norma(lista):
    norma = 0
    posição = 0
    while posição < len(lista):
        norma = norma + ((lista[posição])**2)
        posição += 1
    return norma