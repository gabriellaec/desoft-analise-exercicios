import math
def calcula_gaussiana(σ,x,μ):
    y= 1/(σ*math.sqrt(2*math.pi))*math.exp(-0,5*((x-μ)/σ)**2)
    return y
