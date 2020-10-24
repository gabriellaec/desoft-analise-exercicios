from math import sqrt, sin

g = 9.8

def calcula_distancia_do_projetil (v, teta, h):
    divisao_a = (v**2/2*g) 
    numerador = 2*g*h
    denominador = v**2(sin(teta))**2
    d = divisao_a * (1 + sqrt(1 + numerador/denominador))* sin(2*h)
    return d 
