import math

def calcula_gaussiana(x, mi, sigma):
    a = 1 / (sigma * math.pi)
    b = exp(-0.5 * (((x - mi) / sigma)) ** 2
    gauss = a * b
    return gauss