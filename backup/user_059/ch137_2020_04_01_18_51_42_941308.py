import math 

def calcula_aceleracao(r, f):
    frps = f/60
    w = 2*math.pi*frps
    ac = (w**2)*r
    return ac