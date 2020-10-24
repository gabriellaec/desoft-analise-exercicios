def encontra_maximo(matriz):
    i = 0
    mx = 0
    while i < 3:
        k = 0
        while k < 3:
            if matriz[i][k] > mx:
                mx = matriz[i][k]
            k+=1
        i+=1
    return mx