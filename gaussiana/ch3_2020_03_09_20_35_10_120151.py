from math import pi, sqrt, exp

def calcula_gaussiana(x, mi, sigma):
    f = (1/(sigma*sqrt(2*pi)))*
    b = exp((-0.5*((x-mi)/sigma)**2))
    return f*b