def calcula_gaussiana (x,mi,sigma):
    import math
    f = 1/(sigma*(2*math.pi)**1/2) * math.e**(-0.5*(x-mi/sigma)**2)
    return f 