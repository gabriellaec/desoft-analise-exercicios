import math
def calcula_gaussiana(x, μ, σ):
    i = σ*(math.sqrt(2*math.pi))
    a = math.e**(-0.5*((x - μ)/σ)**2)
    z = (1/i)*a
    return z