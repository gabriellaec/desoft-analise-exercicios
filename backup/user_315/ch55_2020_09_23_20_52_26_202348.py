def encontra_maximo (matriz):
    i = 0
    j = 0
    maior = 0 

    while i < 3:
        while j < 3:
            k = abs(matriz[i][j])
            if maior < k:
                maior = k 
            j += 1 
        i += 1 
        j = 0

    return maior