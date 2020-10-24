import math

def calcula_aceleracao(r, f):
    f = f*60
    w = 2*math.pi*f
    ac = w**2 * r
    return ac
    