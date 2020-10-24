import math


def calcula_gaussiana(x, u, o):
    p1 = 1 / o * math.sqrt(2 * math.pi) * math.e
    p2 = -0.5 * ((x - u) / o) ** 2
    return p1 ** p2
