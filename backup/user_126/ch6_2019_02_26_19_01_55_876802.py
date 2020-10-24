def encontra_maximo(matriz):
    n=matriz[0]
    nu=n[0]
    for i in matriz :
        for i2 in i:
            if i2 > nu:
                nu = i2
            else:
                nu=nu
    return nu