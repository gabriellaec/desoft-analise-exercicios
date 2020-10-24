import math

def calcula_gaussiana (x, μ, σ):
    a = σ
    b = ((2 * math.pi)** (1/2)
    c = (((x - μ)/ σ) ** 2)
    d = (1/(a * b)) * math.e ** (-0,5 * c)
    return d