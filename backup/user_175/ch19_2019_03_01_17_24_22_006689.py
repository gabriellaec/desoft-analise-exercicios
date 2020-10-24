from math import *
def calcula_distancia_do_projetil(v, w, h):
    angulo_radianos = w/(180.0)*(pi)
    L = (((v)**2)/20)  
    M = (1 + sqrt(1 + ((20*h)/((v**2)*(sin(angulo_radianos))**2))))
    N = sin(2*angulo_radianos) 
    distancia = (L)*(M)*(N)
    return distancia