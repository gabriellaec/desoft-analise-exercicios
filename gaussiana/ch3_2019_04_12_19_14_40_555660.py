import math
def calcula_gaussiana(x,μ,σ):
    f= (1/(σ*math.sqrt(2*math.pi)))**(-0.5*((x - μ)/σ)**2)
    return f