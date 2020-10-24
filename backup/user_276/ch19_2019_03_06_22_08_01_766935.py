import math
def calcula_distancia_do_projetil(v,theta,y0):
    a = v**2*math.sin(2*theta)/10
    return a
