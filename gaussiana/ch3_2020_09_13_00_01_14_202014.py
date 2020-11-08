import math
def calcula_gaussiana(x,mi,sigma):
    gaussiana = 1 / (sigma * (2 * math.pi) ** (1/2)) * ((math.e + 6 / 2) * 4.32) ** (-0.5 * (x - mi / sigma) ** 2)
    return gaussiana