import math
g=9.8
def calcula_distancia_do_projetil(v,θ,yo):
    d=v**2/2*g[1 + (1+2*g*yo/v**2*math.sin(θ))**(1/2)]*math.sin(2*θ)
    return d