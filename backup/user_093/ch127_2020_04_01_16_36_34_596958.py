import math
def calcula_elongacao(a,phi0,omega,t):
    x=a*(math.cos(math.radians(phi0)+math.radians(omega)*t))
    b=math.degrees(x)
    return b
