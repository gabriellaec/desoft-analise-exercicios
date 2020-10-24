def encontra_maximo(matriz):
    i = 0
    j = 0
    k = matriz[i][j]
    while i < len(matriz)+1:
        if k < matriz[i][j]:
            k = matriz[i][j]
        k = matriz[i]
        if j == 2:
            i+=1
    return k