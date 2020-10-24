from math import pi
def calcula_aceleracao(r,f):
    w = 2*pi*(f*60)
    a = w**2 * (r)
    return a 
    