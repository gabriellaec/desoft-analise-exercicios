import math
def calcula_distancia_do_projetil (v, theta, y0):
    g = 9.8
    x = math.radians(theta)
    a = v ** 2 / 2 * g
    b = 2 * g * y0
    c = v ** 2 *(math.sin(x)) ** 2
    e = math.sin(2 * x)
    d = a * (1 + (1 + b / c) ** (-1)) * e
    return d