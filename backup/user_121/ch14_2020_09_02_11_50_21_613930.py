import math

def calcula_distancia_do_projetil(v, a, h):
    w = v ** 2 / (2 * g)
    x = 2 * g * h
    y = v ** 2 * math.sin(math.radians(a)) ** 2
    z = math.sin(math.radians(2 * a))
    g = 9.8
    d = w * (1 + math.sqrt(1 + x / y)) * z
    return d