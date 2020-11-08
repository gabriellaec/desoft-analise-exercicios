import math


def calcula_gaussiana(x, m, s):
    return ((1 / (s * math.sqrt(math.pi * 2)) * math.exp (- 0.5 * (x - m / s) ** 2))