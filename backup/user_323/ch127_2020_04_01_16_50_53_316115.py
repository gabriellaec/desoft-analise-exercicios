import math
def calcula_elongacao(A,phiO,omega,t):
    x=A*math.cos(phiO+omega*t)
    return x
