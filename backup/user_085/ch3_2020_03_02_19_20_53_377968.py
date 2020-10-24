import math
def calcula_gaussiana(x, u, o):
    return (1 / o * (math.pi * 2) ** 0.5) * math.e ** (- 0.5 * (x - u / o) ** 2)