import math
def calcula_gaussiana(x,μ,σ):
    return (1/σ*math.sqrt(math.pi*2))**(-0.5*((x-μ)/σ)**2)