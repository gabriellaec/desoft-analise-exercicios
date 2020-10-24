import math

def calcula_gaussiana(x, μ, σ):
    F = (math.e**(-1/2)*(x-μ/σ)**2)/(σ(2*math.pi)**1/2)
    return F
