import math
def calcula_distancia_do_projetil(v,y0,θ):
    d=(v**2/2*g)*math.sin(2*θ)*(1+math.sqrt(1+(2*g*y0)/((v**2)*(math.sin(θ))**2)))
    return d
g=9,8