import math

def calcula_trabalho (F,teta,s):
    teta_rad=math.radians(teta)
    w=F*s*math.cos(teta_rad)
    return w