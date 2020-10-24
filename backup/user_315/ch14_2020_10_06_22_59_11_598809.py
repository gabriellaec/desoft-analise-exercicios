from math import *
g = 9.8
def calcula_distancia_do_projetil(v,teta,y0):
    a = (1+(2*g*y0)/(v**2)*sin(teta)**2)**0.5
    b =  1 + (a*sin(teta))*2
    d = ((v**2)/2*g)*b 
    return d

