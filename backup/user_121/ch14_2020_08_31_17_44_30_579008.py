import math
def calcula_distancia_do_projetil(v, a, h):
    g = 9.8
    d = (v ** 2 / (2 * g)) * math.sin(math.radians(2 * a)) * ((1 + (1 + (2 * g * h) / (v ** 2 * math.sin(math.radians(a)) ** 2))) ** (1/2)) 
    return d