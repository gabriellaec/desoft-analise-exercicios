def calcula_gaussiana(x,mi,sigma):
    import math
    y=math.exp(-0.5*((x-mi)/sigma)**2)/(sigma*(2*math.pi)**1/2)
    return y