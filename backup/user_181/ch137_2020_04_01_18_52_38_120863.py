def calcula_aceleracao(r,f):
    import math
    w = 2*math.pi*(f/60)
    a = (w**2)*r
    return a