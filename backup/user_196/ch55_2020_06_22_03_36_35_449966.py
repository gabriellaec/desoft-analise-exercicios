def encontra_maximo(matriz):
    valorabs = abs(matriz[0][0])
    for i in matriz:
        for c in i:
            if abs(c) > valorabs:
                valorabs = abs(c)
    return valorabs