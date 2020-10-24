def encontra_maximo (matriz):
    i = 0
    while i < len(matriz):
        if matriz[i] > matriz [i+1]:
            return matriz[i]
            i += 1
        else:
            return matriz[i+1]
            i+=1