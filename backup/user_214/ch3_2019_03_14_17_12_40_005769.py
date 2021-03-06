import math

def calcula_gaussiana(x, μ, σ):
    return (1/(σ*((2*math.pi)**(1/2))))**(-0,5*((x-μ)/σ)**2)
                                              