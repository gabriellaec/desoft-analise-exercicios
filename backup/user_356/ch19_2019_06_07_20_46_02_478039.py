import math
def calcula_distancia_do_projetil(v, g, yo,  o):
    d=(v**2/(2*g))*(1+(1+(2*g*yo)/(v**2*(math.sin(math.radians(o)))**2))**1/2)*(math.sin(math.radians(2*o)))
    return d