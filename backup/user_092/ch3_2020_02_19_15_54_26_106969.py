import math
def calcula_gaussiana(x,μ,σ):
    return((1/σ*sqrt(2math.pi))*e**(-0.5*(x-μ/σ)**2))