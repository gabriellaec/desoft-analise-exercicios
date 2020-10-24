import math
def calcula_elongacao(A,phiO,o,t):
    a=math.radians(phiO)
    b=math.radians(o)
    r=a+(b*t)
    z=math.cos(r)
    x=A*(z)
    return x