import math
g = 9.8

def calcula_distancia_do_projetil(v, y0, t0):
    a = v**2 / (2*g)
    b = (2 * g *y0) / ((v ** 2) * math.sin(t0 ** 2))
    c = 1 + math.sqrt(1 + b)
    d = math.sin(2 * t0)
    x = a * c * d
    return x