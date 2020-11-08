import math
def calcula_gaussiana (x,mi,sigma):
    y= 1/sigma*(2**1/2*math.pi)*math.e**(-0.5*(x-mi/sigma)**2)
    return y