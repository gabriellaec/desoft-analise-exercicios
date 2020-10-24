import math
def calcula_norma(lista):
    a = len(lista)
    b = 0
    for i in range(a):
        a = lista[i]
        b += a ** 2
    c = math.sqrt(b)
    return c
        