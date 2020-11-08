import math
def calcula_gaussiana (x, μ, σ):
    a = (σ * ((2 * math.pi)**1/2))
    b = math.e
    c = (((x - μ)/ σ) ** 2)
    d = (1 / a) * b * (-0,5 * c)
    return d
    