import math


def calcula_gaussiana(x, m, s):
    return (1 / s * (math.pi * 2) ** 0.5) * math.e ** (- 0.5 * (x - m / s) ** 2)