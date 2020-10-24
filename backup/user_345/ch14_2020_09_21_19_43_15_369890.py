import math
g = 9.8

def calcula_distancia_do_projetil (v,angulo,y0):
    d = (v**2.0/2*g)(1.0+(1.0 + ((2.0*g*y0)/(v**2)*(math.sin(angulo)**2))* math.sin(2.0*angulo)
    return d
