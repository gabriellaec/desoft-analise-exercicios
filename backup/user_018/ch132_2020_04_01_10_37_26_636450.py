import math
def calcula_trabalho(f,tetagraus,smetros):
    tetarad = math.radians(tetagraus)
    skm = smetros/1000
    t = f*math.cos(tetarad)*skm
    return t