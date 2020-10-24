import math
def calcula_norma(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]**2
    return math.sqrt(s)
    