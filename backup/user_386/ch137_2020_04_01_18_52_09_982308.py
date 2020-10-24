import math
def calcula_aceleracao(r,hz):
    f=hz/60
    w = 2*math.pi*f
    ac = w**2 * r
    return ac