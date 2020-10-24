import math
g = 9.8
def calcula_distancia_do_projetil(v,theta,y0):
    o = math.radians(theta)
    d = (v**2/2*g)*(1+math.sqrt(1+2*g*y0/((v**2)*((math.sin(o))**2))))*math.sin(2*o)
    return d