import math
def calcula_gaussiana(x,μ,σ):
    s=(1/σ*math.sqrt*(2*math.pi))**((-1/2)*((x-μ)/σ)**2)
    return s