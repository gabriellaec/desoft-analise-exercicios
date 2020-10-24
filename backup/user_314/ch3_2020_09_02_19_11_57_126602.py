import math
def calcula_gaussiana(x,μ,σ):
    resultado= math.exp(-0.5*((x-μ)/σ)**2)/(σ*math.sqrt(2)*math.pi)
    return resultado