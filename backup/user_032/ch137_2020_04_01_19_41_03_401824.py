import math
def calcula_aceleracao(r,f):
    w = 2 * math.pi * f
    a =((w*60)**2)* r
    return a