import math
def calcula_elongacao(A,phiO,o,t):
    r=phiO+(o*t)
    z=math.cos(r)
    g=math.degrees(z)
    x=A*(g)
    return x