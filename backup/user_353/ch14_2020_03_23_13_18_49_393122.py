import math
def calcula_distancia_do_projetil(v,θ,y,g):
    return v**2/2g(1+(1+2*g*y/v**2(math.sin(θ))**2)**1/2)*math.sin(2*θ)
