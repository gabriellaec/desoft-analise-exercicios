import math
def calcula_distancia_do_projetil(v,θ,h):
    g = 9.8
    d= v**2/2*g*(1+math.sqrt(1+2*g*h/v**2*math.sin(θ)**2))*math.sin(2*θ)
    return d