import math
def calcula_aceleracao(r,f):
    f = f/60
    omega = 2*f*math.pi
    a = (omega**2)*r
    return a