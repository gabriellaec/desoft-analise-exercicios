def encontra_maximo(matriz):
    maior = 0
    i = 0
    n = 0
    while i < len(matriz):
        while n<len(matriz[0]):
            if matriz[i][n] > maior:
                maior = matriz[i][n]
            n+=1
        i+=1
        n=0
    return maior