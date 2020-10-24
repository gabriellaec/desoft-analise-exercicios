import math
def calcula_distancia_do_projetil (v, o, h):
    return ((v**2 / 19.6) * (1 + (1+ (2*9.8*h)/ v**2 * ((math.sin(o))**2))* math.sin(20)))