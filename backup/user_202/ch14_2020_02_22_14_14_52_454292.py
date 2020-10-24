import math
def calcula_distancia_do_projetil(v,o,y):
    g = 9.8
    return((v**2*(1+math.sqrt(1+2*g)))/2*g)