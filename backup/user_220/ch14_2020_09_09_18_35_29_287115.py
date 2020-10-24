import math

def valor_sen(θ):
    seno = math.sin(θ)
    return seno

g=9.8

def calcula_distancia_do_projetil(v,θ,yo):
    d = v**2 / 2 * g [1 + (1 + 2 * g * yo / v**2 * seno)**(1/2)] * 2 * seno
    return d