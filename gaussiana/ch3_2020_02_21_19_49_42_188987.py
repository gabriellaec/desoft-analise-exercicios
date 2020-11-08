import math


def calcula_gaussiana(a, b, c):
    p = (math.exp(-(((a-b)/c)**2)*1/2))/(c*((2*math.pi)**(1/2)))
    return p