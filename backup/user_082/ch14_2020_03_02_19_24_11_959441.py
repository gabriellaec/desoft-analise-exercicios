import math
g=9.8
def calcula_distancia_do_projetil (v, o, h):
    return ((v**2 / 2*g) * (1 + (1+ (2*g*h)/ v**2 * ((math.sin(o))**2))* math.sin(20)))