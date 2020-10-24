def encontra_maximo(matriz):
    nu=matriz[0][0]
    for i in matriz :
        for i2 in i:
            if abs(i2) > nu:
                nu = abs(i2)
    return nu