import math
def calcula_elongacao(A,phiO,omega,t):
    x=A*math.cos((phiO*math.pi)/180+omega*t)
    return x
