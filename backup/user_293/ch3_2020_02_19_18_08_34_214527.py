import math
def calcula_gaussiana(x,μ,σ):
    a = 1/(σ*(math.sqrt(2*math.pi))
    b = math.exp(-0.5*(((x-μ)/σ)**2))
    c = a*b
    return c