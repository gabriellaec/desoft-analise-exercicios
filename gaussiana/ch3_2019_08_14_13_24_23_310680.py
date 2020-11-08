import math

def calcula_gaussiana(x, u, o):
    return 1 / o * ((2 * math.pi) ** (1 / 2)) * math.exp(-0.5 * ((x - u) / o) ** 2)