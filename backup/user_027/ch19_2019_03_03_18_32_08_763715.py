from math import *
g = 9.8
def calcula_distancia_do_projetil(v,theta,y):
    A = ((v**2)/(2*g))
    B = (sin(2*theta))
    C = sqrt(1+((2*g*y)/((v*sin(theta))**2)))
    return (A*(1+C)*B)
