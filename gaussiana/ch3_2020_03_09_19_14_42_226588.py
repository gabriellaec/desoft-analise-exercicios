import math
def calcula_gaussiana(x, mi, sigma):
    a = 1 / sigma*math.sqrt(2*math.pi)
    b = -0,5*((x - mi) / sigma)**2
    formula = a * (math.e)**b
    return formula