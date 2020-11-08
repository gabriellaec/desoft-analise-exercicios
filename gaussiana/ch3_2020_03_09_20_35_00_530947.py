import math
def calcula_gaussiana(x, m, o):
    c=1/(o*((2*math.pi)**0.5))
    b=(math.e**[-0.5*(x-m/o)*2])
    z=b*c
    return z