import math
def calcula_gaussiana (x, μ, σ):
    a = 1 / (σ * ((2 * math.pi)**1/2))
    b = math.e 
    c = (-0,5 * (((x - μ)/ σ) * 2))
    d = a * (b ** c)
    return d
    