import math
def calcula_distancia_do_projetil(v, y, θ):
    x = v**2**math.sin(2*θ)/(2*9.8)*(1+(1+(2*9.8*y)/(v**2*math.sin(θ)**2))**(1/2))
    return x                 