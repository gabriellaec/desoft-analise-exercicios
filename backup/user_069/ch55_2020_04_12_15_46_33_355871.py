def encontra_maximo (matriz):
    maximo = matriz[0][0]
    for e in matriz:
        if e > maximo:
            maximo = e
    return maximo