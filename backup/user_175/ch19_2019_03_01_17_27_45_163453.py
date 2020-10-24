from math import *
def calcula_distancia_do_projetil(v, w, h):
    g = 9.8
    L = (v**2)/(2*g)  
    M = 1 + sqrt(1 + ((2*g*h)/((v**2)*(sin(w)**2))
    N = sin(2*w) 
    distancia = L*M*N
    return distancia