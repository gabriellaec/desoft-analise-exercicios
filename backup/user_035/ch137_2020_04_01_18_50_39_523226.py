import math
def calcula_aceleracao(r, f):
    omega = 2*math.pi*f
    ac = omega**2*r
    return ac