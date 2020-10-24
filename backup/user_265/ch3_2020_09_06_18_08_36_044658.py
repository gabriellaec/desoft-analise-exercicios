import math
def calcula_gaussiana (x,μ,σ):
    g = ((1/(σ *((2 * math.pi) ** 0,5))) * (math.e ** (-0.5 * (((x - μ)/σ) ** 2))))
    return g
