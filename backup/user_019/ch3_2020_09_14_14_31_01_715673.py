import math
def calcula_gaussiana (x,mu,sigma) :
    f1 = 1/sigma*math.sqrt2*math.pi
    f2 = e**((-0.5*(x-mu)/(sigma))**2)
    y = f1*f2
    return y