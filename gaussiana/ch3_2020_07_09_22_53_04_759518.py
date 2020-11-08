import math


def calcula_gaussiana(x, u, o):
    return math.pow(1 / (o * math.sqrt(math.pi * 2)), (-0.5 * math.pow(((x - u) / o), 2)))
