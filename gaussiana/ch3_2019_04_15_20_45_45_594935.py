import math
def calcula_gaussiana(x, mi, sigma):
    if sigma != 0:
    gaussiana = (1 / (sigma * math.sqrt(2 * math.pi))) ** (-0.5 * ((x - mi) / sigma) ** 2)
    return gaussiana