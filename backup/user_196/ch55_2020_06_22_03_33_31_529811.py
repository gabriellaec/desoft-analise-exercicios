def encontra_maximo(matriz):
    valorabs = abs(matriz[0][0])
    for i in matriz:
        for abs(c) in i:
            if abs(c) > valorabs:
                valorabs = abs(c)
            else:
                valorabs = valorabs
    return abs(valorabs)