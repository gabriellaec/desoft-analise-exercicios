import math
def calcula_gaussiana(x,μ,σ):
    return(1/(σ*math.sqrt(2*math.pi))*math.exp**(-0.5*(((x-μ)/σ)**2))