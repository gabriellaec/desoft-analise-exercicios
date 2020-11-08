from numpy import exp
from math import sqrt, pi


def calcular_gaussiana(x, mi, sigma):
    return exp(1) ** (-0.5*((x - mi) / sigma) ** 2) / sigma * sqrt(2 * pi)
