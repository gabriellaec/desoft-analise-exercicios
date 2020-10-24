from math import*
def calcula_distancia_do_projetil(v, θ, y):
    g = 9*8
    a = v**2/2*g
    b = 1 + (1 + 2*g*y/(v**2)*(sin(θ))*2)**0.5
    c = sin(2*θ)
    x = a*b*c
    print(x)
    return x