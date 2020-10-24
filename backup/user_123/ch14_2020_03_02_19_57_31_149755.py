import math

def calcula_distancia_do_projetil(v,teta,y):
    g = 9,8
    a = ((v ** 2)/2*g)* sin(2 teta)
    b = 1 + ( 1 + ((2 * g * y) / ((v ** 2) * ((sin(teta)) ** 2) ** (1/2))
    c = a * b
    return c