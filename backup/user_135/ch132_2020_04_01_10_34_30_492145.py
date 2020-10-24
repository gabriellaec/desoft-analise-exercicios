import math

def calcula_trabalho(forca, cos_teta, s):
    trabalho = forca * math.cos(math.radians(cos_teta)) * s
    return trabalho