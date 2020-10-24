import math
def calcula_trabalho (F, teta, s):
    teta = math.radians(teta)
    trabalho = F * (math.cos(teta)) * s
    return trabalho