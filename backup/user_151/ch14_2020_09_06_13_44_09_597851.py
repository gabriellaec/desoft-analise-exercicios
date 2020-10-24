import math
def calcula_distancia_do_projetil(v, T, y0):
    d = (v ** 2 / 2g) * (1 + (1 + 2 * g * y0 / ( v ** 2 * (sin(radians(T))) ** 2)) ** 1/2) * sin(radians(2 * T))
    return d