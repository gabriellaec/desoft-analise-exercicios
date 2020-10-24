import math

def calcula_distancia_do_projetil(v, a, h):
    g = 9.8
    w = v ** 2 / (2 * g)
    x = 2 * g * h
    y = v ** 2 * math.sin(math.radians(a)) ** 2
    z = math.sin(2 * a)
    d = w * (1 + math.sqrt(1 + x / y)) * z
    return d