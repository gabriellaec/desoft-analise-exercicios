from math import sqrt, sin

g = 9.8


def calcula_distancia_do_projetil (v, teta, y0):
    parte1 = (v**2)/2*g
    parte2 = (1 + sqrt(1 + (2*g*y0) / (v**2(sin(teta))**2)))
    parte3 = sin(2*teta)
    d = parte1 * parte2 * parte3
    return d 
