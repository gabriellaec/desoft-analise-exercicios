import math

def calcula_distancia_do_projetil(v, θ, y):
    return (v**2)*math.sin(2*θ)/(2*9.797645)*(1+(1+(2*9.797645*y)/((v**2)*math.sin(θ)**2))**0.5)