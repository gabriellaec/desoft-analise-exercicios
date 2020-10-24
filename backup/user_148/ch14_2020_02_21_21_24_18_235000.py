import math

def calcula_distancia_do_projetil(v, o, y0):
    d = (1+(1+((2*9.8*y0)/(v**2)*(math.sin(o))**2))**(1/2))*((v**2)/(2*9.8))*(math.sin(2*o))
    return d