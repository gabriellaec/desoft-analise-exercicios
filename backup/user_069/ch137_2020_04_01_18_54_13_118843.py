import math
def calcula_aceleracao (r,f):
    w = 2*math.pi*f*1/60
    a = w**2*r
    return a