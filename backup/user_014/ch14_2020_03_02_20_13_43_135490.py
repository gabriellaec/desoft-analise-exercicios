import math
g = 9.8
def calcula_distancia_do_projetil d(v,y0,x):
    a = (v**2/2*g)
    b = (1 + (1 + (2*g*y0)/(v**2)*(sin(x)**2)))**1/2
    c = sin(2*x)
    d = a * b * c
    return d