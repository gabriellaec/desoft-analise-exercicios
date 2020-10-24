from math import sqrt
from math import sin
def calcula_distancia_do_projetil(v,t,y0):
    g = 9.8
    a = (v**2)/(2*g)
    b = 1 + sqrt(1 + ((2*g*y0)/((v**2)*sin(t)**2))
    c = sin (2*t)             
    return  a * b * c