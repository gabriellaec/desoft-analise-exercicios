import math
def calcula_distancia_do_projetil (v,ang,y0):
    d = v**2*(1+(1 + (2*9.8*y0/v**2*(math.sin(ang))**2))**0.5)*math.sin( 2*ang)/2*9.8
    return d