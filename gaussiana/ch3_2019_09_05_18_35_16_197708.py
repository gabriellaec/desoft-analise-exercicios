import math

def calcula_gaussiana(x, u, o):
    a = 1 / (o*(2*math.pi)**0.5)
    b = ((x - u) / o )**2
    return a*math.exp(-0.5*b)