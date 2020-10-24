import math

def calcula_gaussiana(x, mi, sig):
    gaussiana= 1/sig*math.sqrt(math.pi*2)*math.exp(-(1/2)*((x-mi)/sig)**2)
    return gaussiana