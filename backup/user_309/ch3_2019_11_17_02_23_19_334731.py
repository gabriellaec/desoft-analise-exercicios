import math
def calcula_gaussiana(x,mi,sigma):
    x = sigma*((2*math.pi)*(1/2))
    y = math.exp(-0.5*((x-mi)/sigma)**2)
    f = 1/x*y
    return f
