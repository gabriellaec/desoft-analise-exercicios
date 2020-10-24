import math
def calcula_gaussiana(x,mi,sigma):
    expo=(-0.5)*((x-mi)/sigma)**2
    f=(1/(sigma*(2*pi)**0.5))*exp(expo)
    return f
