import math

def calcula_gaussiana(x, mi, sig):
    f=(1/sig*math.sqrt(2*math.pi)*math.exp(-0.5*((x-mi/sig)**2)
    return f