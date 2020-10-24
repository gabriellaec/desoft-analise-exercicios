import math


def calcula_gaussiana(a, b, c):
    p = (math.exp(-(((a-b)/c)**2)*1/2)/((2*math.pi*c**2)**1/2))
    return p