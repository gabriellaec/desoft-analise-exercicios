from math import*
def calcula_distancia_do_projetil(v, θ, y):
    g = 9.8
    a = (v**2 / (2 * g))
    b = (1 + sqrt(1 + ((2 * g * y)/v**2 * (sin(θ))**2)))
    c = sin(2 * θ)
    return(a * b * c)