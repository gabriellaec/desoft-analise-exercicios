from math import *
g=9.8
def calcula_distancia_do_projetil(v,O,y):
    d=(v**2/2*g)*(1+sqrt(1+(2*g*y/v**2(sin(O))**2)))*sin(2*O)
    return d