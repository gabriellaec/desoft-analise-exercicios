def encontra_maximo (matriz):
    matriz[0] = [matriz[0][0], matriz[0][1], matriz[0][2]]
    matriz[1] = [matriz[1][0], matriz[1][1], matriz[1][2]]
    matriz[2] = [matriz[2][0], matriz[2][1], metriz[2][2]]
    maximo = matriz[0][0]
    for e in matriz:
        if e > maximo:
            maximo = e
    return maximo