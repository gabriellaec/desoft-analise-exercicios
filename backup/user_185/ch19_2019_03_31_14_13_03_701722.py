import math
def calcula_distancia_do_projetil(a,b,c):
    a = v**2 / 2g
    b = 2gy0 / v**2 * (math.sin(θ))**2
    c = math.sin(2θ)
    distancia = a * (1 + math.sqrt(1 + b)) * c
    return distancia