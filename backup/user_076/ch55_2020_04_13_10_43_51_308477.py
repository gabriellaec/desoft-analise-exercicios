def encontra_maximo (matriz):
    i = 0
    c = 0
    while i < len(matriz):
        while c-1 < len(matriz[i]):
            if matriz[i][c] > matriz[i][c+1]:
                x = matriz[i][c]
            c+=1
        i+=1
    return x