import math
def calcula_trabalho (forca, ang, s):
    ang = math.radians(ang)
    trab = forca * (math.cos(ang)) * s
    return trab