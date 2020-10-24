import math
def calcula_elongacao(A,phiO,omega,t):
    x=A*math.cos((phiO*180)/math.pi+omega*t)
    return x
