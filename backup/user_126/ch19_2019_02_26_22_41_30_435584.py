import math
def calcula_distancia_do_projetil (v,teta,y0,g):
    d=v**2/2*g*(1+(2*g*y0/v**2*math.sin(teta)**2)**0.5)*math.sin(20)
    return d