import math
def calcula_distancia_do_projetil(v,o,y0):
    y=(v**2/(19.6)*((1+(1+(19.6*y0)/(v**2*math.sin(o)**2))**0.5))*math.sin(2*o)
    return y