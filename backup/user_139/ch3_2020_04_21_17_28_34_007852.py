import math
def calcula_gaussiana (x, mi, sigma):
    a = sigma * (2 * math.pi) ** (1/2)
    b = ((x - mi) / sigma) ** 2
    c = -0.5 * b
    d = (1 / a) * math.e ** c
    return d
