import math
def calcula_distancia_do_projetil(v, T, y0):
    g = 9,8
    d = (v ** 2 / 2g) * (1 + (1 + 2 * g * y0 / ( v ** 2 * (sin(T)) ** 2)) ** 1/2) * sin(2T)
    return d