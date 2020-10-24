import math
def calcula_elongacao(A,phi0,omega,t):
    x=A*math.cos(math.radians(phi0+omega*t))
    return x
x=calcula_elongacao
print(x)