import math
def calcula_gaussiana(x,mi,sigma):
    Y=1/sigma*(math.exp(-0.5*((x-mi)/sigma)**2))
    return Y