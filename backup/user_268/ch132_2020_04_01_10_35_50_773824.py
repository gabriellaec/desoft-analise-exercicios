import math
def calcula_trabalho(F, o, s):
    rad= math.radians(o)
    trab= F * (math.cos(rad)) * s
    return trab