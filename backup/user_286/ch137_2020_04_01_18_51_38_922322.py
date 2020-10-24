import math

def calcula_aceleracao(r,f):
    f_hz = f/60
    ac = (2*math.pi*f_hz)**2*r
    return ac
