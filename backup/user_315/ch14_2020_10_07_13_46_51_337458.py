from math import *
def calcula_distancia_do_projetil(v,teta,y0):
    g = 9.8
    a = (v**2)/(2*g) 
    b = (1+sqrt(1+(2*g*y0)/(v**2*sin(teta))
    c =  sin(2*teta)
    d = a*b*c 
    return d

