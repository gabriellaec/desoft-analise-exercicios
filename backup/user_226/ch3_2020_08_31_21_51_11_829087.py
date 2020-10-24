import math

def calcula_gaussiana(x, mi, sigma):
    divisor = sigma * (math.sqrt(2 * math.pi))
    dividendo = math.e ** (-0.5 * (((x - mi) / sigma) ** 2))
    resultado = dividendo / divisor

    return resultado