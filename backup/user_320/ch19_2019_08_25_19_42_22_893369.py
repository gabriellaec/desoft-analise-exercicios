from math import sin, sqrt

def calcula_distancia_do_projetil(v, teta, y0):
    g = 9.8
    x1 = (v** 2) / (2* g)
    x2 = 1 + sqrt(1 + ((2*g*y0)/ (v** 2 * sin(teta)**2)))
    x3 = sin(2 * teta)
    return x1 * x2 * x3