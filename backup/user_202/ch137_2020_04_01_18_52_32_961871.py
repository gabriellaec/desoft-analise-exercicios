import math
def calcula_aceleracao(r,f):
    f = f/60
    o = 2*math.pi*f
    ac = r*o**2
    return(ac)