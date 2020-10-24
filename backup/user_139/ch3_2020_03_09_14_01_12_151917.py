import math
def calcula_gaussiana(x, mi, sigma):
    a = 1 / b
    b = sigma * (2 * math.pi) ** (1/2)
    c = ((x - mi) / sigma) ** 2
    d = -0.5 * c
    f = a * math.e ** d
    return f