import math
math.pi
def calcula_gaussiana(x,μ,σ):
    g = (1/(σ * ((2 * pi) ** 0.5))) * (e ** (-0.5 * (((x - μ)/σ) ** 2)))
    return g