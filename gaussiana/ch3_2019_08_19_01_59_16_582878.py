def calcula_gaussiana(x, μ, σ):
    import math
    return (1/σ*((2*math.pi)**1/2))*math.e**(-0.5*(((x-μ)/σ))**2)