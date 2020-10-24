import math
def calcula_distancia_do_projetil(v,θ,y0):
    d = v**2/19.6*(1+(1+(19.6*y0)/(v**2*math.sin(θ)))**0.5*math.sin(2*θ)
    return d