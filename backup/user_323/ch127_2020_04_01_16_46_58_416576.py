import math
A=0.5
phiO=0
omega=10
t=1
def calcula_elongacao(A,phiO,omega,t):
    x=A*(math.cos(phiO)+omega*t)
    return x
