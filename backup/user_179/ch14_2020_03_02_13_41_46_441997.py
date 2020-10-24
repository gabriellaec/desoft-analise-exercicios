import math
def calcula_distancia_do_projetil (v,θ,y0):
    g = 9,8

    a = (v**2)/2*g
    b = 1 + (1+(2*g*y0)/(v**2*math.sin(θ)**2)) **(1/2)
    c = math.sin(2*θ)
    distancia = a*b*c
    return distancia