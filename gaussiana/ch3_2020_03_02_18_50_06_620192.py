import math

def calcula_gaussiana(a,b,c):
    return ((1 / c * (2*math.pi)**1/2) * math.e** -0.5*((a-b/c)**2))