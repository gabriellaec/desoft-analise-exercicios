from math import sqrt, sin

def calcula_distancia_do_projetil (v, teta, h):
    g = 9.8
    a = (v**2/2*g) 
    b = 2*g*h
    c = v**2(sin(teta))**2
    d = a * (1 + sqrt(1 + b/c))* sin(2*h)
    return d 
