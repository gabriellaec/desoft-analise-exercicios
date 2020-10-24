def encontra_maximo(matriz):
    valorabs = matriz[0][0]
    for i in matriz:
        for c in i:
            if c > valorabs:
                valorabs = c
            else:
                valorabs = valorabs
    return abs(valorabs)