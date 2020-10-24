import math
def calcula_distancia_do_projetil(v,o,y0):
    d = (v**2/2*g)*(1+math.sqrt(1+2*g*y0/v**2((math.sin(o))**2))*math.sin(o)
    return d