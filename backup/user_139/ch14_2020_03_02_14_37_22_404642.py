import math
g = 9.8
def calcula_distancia_do_projetil (v, x, y0):
    a = v ** 2 / 2 * g
    b = 2 * g * y0
    c = v ** 2 *(math.sin(x)) ** 2
    e = math.sin(2 * x)
    d = a * (1 + (1 + b / c) ** (1/2)) * e
    return d