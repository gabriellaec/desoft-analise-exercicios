import math


def calcula_gaussiana(x, m, s):
    return 1 / (s * (math.sqrt (2*math.pi))) * math.exp (-0.5 * (x - m / s) ** 2)