import math
def calcula_distancia_do_projetil(v, T, y):
    d = (v ** 2 / 2 * float(9.8)) * (1 + (1 + 2 * float(9.8) * y / ( v ** 2 * (math.sin(T)) ** 2)) ** 1/2) * math.sin(2 * T)
    return d