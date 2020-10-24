def encontra_maximo(matriz):
    valor_max = 0
    e = 0
    while e <= 3:
        i = 0
        while i <= 3:
            if matriz[e][i] > valor_max:
                valor_max = matriz[e][i]
                i += 1
            else:
                i += 1
        e += 1
    return valor_max