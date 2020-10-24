import math
def calcula_aceleracao(r,f):
    s = f * 60
    va = math.pi*2*s
    ac = (va**2)*r
    return ac