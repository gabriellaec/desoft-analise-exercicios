import math

g=9.8

def calcula_distancia_do_projetil(v,sin(θ),yo):
    d = v**2 / 2 * g [1 + (1 + 2 * g * yo / v**2 * (sin(θ)**2))**(1/2)] * 2 * sin(θ)
    return d