import math


def calcula_distancia_do_projetil(v, a, h, g):
    return ((v ** 2) / 2 * g) * (1 + math.sqrt(1 + (2 *g * h) / ((v ** 2) * (math.sin(a)) ** 2))) * math.sin(2 * a)