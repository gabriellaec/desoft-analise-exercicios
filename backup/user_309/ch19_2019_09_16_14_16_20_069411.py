import math

def calcula_distancia_do_projetil(v,teta,y0):
    g = 9.8
    a = 2*g*y0
    o = (v**2)*(math.sin(teta)**2)
    dist = (v**2)/(2*g)*(1 + a/o)*math.sin(2*teta)
    return dist