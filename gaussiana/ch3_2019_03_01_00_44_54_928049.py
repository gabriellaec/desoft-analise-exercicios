import math

def caucula_gaussiana(x, mi, sig):
    f=(1/sig*math.sqrt(math.pi*2))*math.exp(-0.5((x-mi)/sig)**2)
    return f