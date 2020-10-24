import math
def calcula_distancia_do_projetil(g, z, v, x):
    y = v ** 2 / (2*g) *(1 + (1 + (2*g*z/ v ** 2 * (math.sin(x)) ** 2)** (1/2))) * math.sin(2*x)
    return y
    