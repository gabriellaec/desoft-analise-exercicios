from math import *
def calcula_distancia_do_projetil(v,theta,y):
    g = 9.8
    A = ((v**2)/(2*g))
    B = 2*g*y
    C = ((v*sin(theta))**2)
    D = sin(2*theta)
    E = sqrt(1+(B/C))
    return (A*(1*E)*D)