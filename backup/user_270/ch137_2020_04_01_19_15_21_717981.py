import math
def calcula_aceleracao(r,f):
    f = f/60
    w = 2*math.pi*f
    a = (w**2)*f
    return a