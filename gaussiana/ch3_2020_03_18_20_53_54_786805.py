import math

def calcula_gaussiana (x, μ, σ):
    a = σ * (2 *(math.pi)) ** (1/2)
    b = ((x - μ)/ σ) ** 2
    c = (1/a) * (math.e) ** (-0,5 * b)
    return c