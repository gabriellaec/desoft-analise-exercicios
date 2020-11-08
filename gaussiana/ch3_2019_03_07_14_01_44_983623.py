import math 
def calcula_gaussiana(x,μ,σ):
    g= math.exp(-0.5*(((x - μ)/σ)**2))/(σ*((0.5 * (math.pi))**0.5))
    return g

