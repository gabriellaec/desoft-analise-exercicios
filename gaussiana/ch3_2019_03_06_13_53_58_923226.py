import math.exp(x)
def calcula_gaussiana(x,mi,sigma):
    y=1/(sigma*(2*pi)**0.5)*exp(-0.5*(x-mi/sigma)**2)
    return y