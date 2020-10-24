import math
def calcula_trabalho(f,tetagraus,smetros):
    tetarad = math.radians(tetagraus)
    t = f*math.cos(tetarad)*smetros
    return t