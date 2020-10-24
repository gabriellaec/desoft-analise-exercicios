import math
def calcula_aceleracao(r,f):
    n = f/60
    w = 2*math.pi*n
    a = (w**2)*r
    return a