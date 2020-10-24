import math
def calcula_distancia_do_projetil(v,θ,y0):
    dist = (v**2/2*19.6)*(1 + ((1 + 9.8*y0)/(v**2 *((math.sin(θ))**2)**(1/2))*math.sin(2*θ))
    return dist
a = calcula_distancia_do_projetil(0, math.pi/4, 0)
    print(a)