from math import *
def calcula_distancia_do_projetil(h, v, w):
    L = ((v**2)/2*10)  
    M = sqrt(1 + ((2*10*h)/((v**2)*(sin(w))**2)))
    N = sin(2*w) 
    distancia = L*(1 + M)*N
    return distancia