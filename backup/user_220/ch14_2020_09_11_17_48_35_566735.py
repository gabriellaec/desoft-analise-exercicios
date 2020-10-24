import math

def calcula_distancia_do_projetil(v,θ,yo):
    d = v**2 / (2 * 9.8) * (1 + (1 + 2 * 9.8 * yo / (v**2 * (math.sin(θ))**2))**(1/2)) * math.sin(2*θ)
    return d