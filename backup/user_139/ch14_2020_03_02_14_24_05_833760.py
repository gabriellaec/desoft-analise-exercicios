import math
def calcula_distancia_do_projetil (v, θ, y0):
    g = 9.8
    d = math.radians(θ)
    a = v ** 2 / 2 * g
    b = 2 * g * y0
    c = v ** 2 *(math.sin(d)) ** 2
    e = math.sin(2 * d)
    D = a * (1 + (1 + b / c) ** (-1)) * e
    return D