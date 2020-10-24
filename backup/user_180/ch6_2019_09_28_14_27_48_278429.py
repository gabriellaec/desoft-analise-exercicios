def encontra_maximo(matriz):
    variable = 0
    for i in matriz:
        for a in i:
            if a > variable:
                variable = a
    return variable