import math
def calcula_distancia_do_projetil(v, T, y):
    d = (v ** 2 / 2 * floot(9.8)) * (1 + (1 + 2 * floot(9.8) * y / ( v ** 2 * (sin(radians(T))) ** 2)) ** 1/2) * sin(radians(2 * T))
    return d