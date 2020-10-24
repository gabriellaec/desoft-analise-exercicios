import math

def calcula_distancia_do_projetil(v, h, y0)
    distancia = v ** 2 / 2 * 9.8 * (1+ (math.sqrt(1 + ((2 * 9.8 * y0) / (v ** 2 * (math.sin(h))) ** 2)) * math.sin(2 * h) 
    return distancia