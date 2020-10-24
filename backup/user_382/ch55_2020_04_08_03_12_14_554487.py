import numpy as np
def encontra_maximo(lista):
    lista2 = []
    for i in lista:
        for t in i:
            lista2.append(np.abs(t))
    return max(lista2)