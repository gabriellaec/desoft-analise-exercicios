import math
def encontra_maximo(matriz):
    x=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if module(matriz[i][j])>x:
                x=matriz[i][j]
    return x
        