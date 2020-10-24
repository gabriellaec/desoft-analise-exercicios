from math import sin
from math import sqrt

def calcula_distancia_do_projetil(v,teta,y0):
    g = 9.8
    x = ((v**2)/(2*g))
    y1 = 2*g*y0
    y2 = (v**2)*(sin(teta)**2)
    z = sin(2*teta)
    d = x*(1+sqrt(1+(y1/y2)))*z
    return d
