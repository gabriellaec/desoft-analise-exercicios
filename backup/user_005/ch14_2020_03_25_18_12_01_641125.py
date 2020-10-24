import math
def calcula_distancia_do_projetil (v,o,y,g):
    g=9.8
    d = v**2/2*g(1+(1+(2*g*Y)/(v**2*(math.sin(o))**2))**(1/2))*math.sin(2*o)
    return d 