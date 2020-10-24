import math
def calcula_aceleracao(r,F):
    f = F/60
    w = math.pi*2*f
    a = (w**2)*r
    return a