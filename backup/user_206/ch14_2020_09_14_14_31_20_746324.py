import math
def calcula_distancia_do_projetil(v, a, h):
    d = v ** 2 / 19.6 * ( 1 + math.sqrt(1 + 19.6 * h / ( v ** 2 * ( math.sin(a) ** 2)) * math.sin(2 * a)
    return(d)