import math


def calcula_gaussiana(x, u, o):
    return (1 / (o * math.sqrt(2 * math.pi))) * math.e ** (-0.5 * ((x-u) / o)**2)
