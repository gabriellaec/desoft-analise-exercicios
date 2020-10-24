import math
def calcula_trabalho(F, teta, s):
    a = math.radians(teta)
    b = math.cos(a)
    trabalho = F*b*s
    return trabalho