def encontra_maximo(matriz):
    maximo = abs((matriz[0])[0])
    for i in matriz:
        for j in i:
            if abx(j) >maximo:
                maximo = abs(j)
    return maximo