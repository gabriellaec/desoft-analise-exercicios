import math


def calcula_distancia_do_projetil(v, o ,  yo):
    rad= o * math.pi / 180
    d = v**2/19.6 (1 + math.sqrt(1 + 2*9.8*yo/v**2*(math.sin(rad)**2))) * math.sin((2*rad))
    return d