import math
p = math.pi
def calcula_gaussiana(x, m, s):
    return (1 / s * ((2 * p) ** 0.5)) ** (-0.5 * (x - m / s) ** 2)
