import math
def calcula_distancia_do_projetil(v,teta,y0):
    g = 9.8
    a = v**2/(2*g)
    b = (2*g*y0)/((v**2)*math.sin(teta)**2)
    d = a*(1 + (1 + b)**0.5)*math.sin(2*teta)
    return d