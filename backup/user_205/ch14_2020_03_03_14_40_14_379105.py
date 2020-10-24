import math

def calcula_distancia_do_projetil (v,y,o):
    g = 9.8
    A = ((v**2)/(2g))*math.sin(2o)
    B = 1 + (1 + ((2*g*y)/(v**2 * math.sin(o)**2)))**(1/2)
    return (A*B)
    