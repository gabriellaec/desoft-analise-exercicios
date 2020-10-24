import math
def calcula_aceleracao(r,f):
    w = 2*math.pi*f*60
    aceleracao = w**2*r
    return aceleracao