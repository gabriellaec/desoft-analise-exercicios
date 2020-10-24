def encontra_maximo(matriz):
    variable = matriz[0][0]
    for i in matriz:
        for a in i:
            if a > variable:
                variable = a
    return variable