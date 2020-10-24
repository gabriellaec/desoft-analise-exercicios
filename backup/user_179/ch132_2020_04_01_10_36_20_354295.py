import math
def calcula_trabalho (F,teta,s):
    teta_radianos = math.radians(teta)
    trabalho = F * math.cos(teta_radianos) * s
    return trabalho