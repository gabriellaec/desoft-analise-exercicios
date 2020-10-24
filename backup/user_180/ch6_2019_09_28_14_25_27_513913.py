def encontra_maximo(matriz):
   	variable = 0
    for i in matriz:
        if i.max() > variable:
            variable = i.max()
    return variable