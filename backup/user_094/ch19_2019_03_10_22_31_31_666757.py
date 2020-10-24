import math
def calcula_distancia_do_projetil (v,ang,y0):
    d = (v**2/2*9.8)*(1+(1 + (2*9.8*y0/v**2(math.sin(math.pi*ang/180))**2))**0.5)*math.sin(math.pi*2*ang/180)
    return d