from math import pi
def calcula_aceleracao(r,f):
    w = 2 * pi*f
    a = w**2 * (r/60)
    return a 
    