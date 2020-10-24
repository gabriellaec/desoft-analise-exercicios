import math
def calcula_elongacao(A,phiO,o,t):
    b=math.radians(phiO)
    c=math.radians(o)
    r=phiO+(o*t)
    z=math.cos(r)
    g=math.degrees(z)
    x=A*(g)
    return x