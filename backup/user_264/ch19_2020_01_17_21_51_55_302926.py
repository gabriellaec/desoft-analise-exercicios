import math

def calcula_distancia_do_projetil(v, teta, y0):
    d = (v**2/2*9.8)*(1+(math.sqrt(1+((2*9.8*y0)/(v**2)*(math.sin(teta)**2)))))*2*math.sin(teta)*math.sin(teta)
    return d