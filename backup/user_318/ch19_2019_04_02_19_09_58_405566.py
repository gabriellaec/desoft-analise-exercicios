import math 
def calcula_distancia_do_projetil(v,o,y0):
    d=(v**2/(2*9.8))*(1+(1+((2*9.8*y0)/(v**2*(sin(o))**2)))**0.5))*sin2o
    return d