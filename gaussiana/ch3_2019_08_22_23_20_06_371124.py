from math import sqrt, pi, exp


def calcula_gaussiana(x, mi, sigma):
    numerador = exp(1) **(-0.5*((x - mi) / sigma) ** 2)
    denomin = sigma * sqrt(2 * pi)
    return numerado / denomin
