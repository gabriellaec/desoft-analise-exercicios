import math
θ = float(input())
θ= math.radians(θ)
def calcula_distancia_do_projetil(v, θ, y0):
    d = ((v**2)/(2 * 9.8))*(1 + math.sqrt(1 + (2 * 9.8 * y0)/(v*math.sin(θ))**2))*math.sin(2*θ)
    return d                   