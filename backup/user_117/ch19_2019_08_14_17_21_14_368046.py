from math import sqrt
from math import sin

def calcula_distancia_do_projetil(v,t, y0):
    g = 9.8
    d = ((v**2)/2*g) * (1 + sqrt(1 + (2 * g * y0)/(v**2) * sin(t)**2)) * sin(2*t)
    return d
