import math
g = 9.8
def calcula_distancia_do_projetil(v,θ,y):
    tmp1 = (v**2)/(2/g)
    tmp2 = 1 + math.sqrt(1 + (2*g*y) / ((v**2) * (math.sin(θ)**2)))
    tmp3 = math.sin(2*θ)
    return tmp1 * tmp2 * tmp3
   