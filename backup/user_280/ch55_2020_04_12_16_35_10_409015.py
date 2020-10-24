def encontra_maximo(matriz):
    a = matriz[0][0]
    for i in matriz:
        for j in i:
            if a < 0:
                a = -a
            if j>a:
                a = j
            if j<a:
                a = a
    return a