import math
def calcula_distancia_do_projetil(v,teta,y0):
    return v**2/(2*9.8)*(1+(1+2*9.8*y0/(v**2*math.sin(teta)**2))**0.5)*math.sin(2*teta)
 