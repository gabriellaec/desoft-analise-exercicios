import math
def calcula_aceleracao(f, r):
    o = f/60
    ac = ((2*math.pi*o)**2)*r
    return ac