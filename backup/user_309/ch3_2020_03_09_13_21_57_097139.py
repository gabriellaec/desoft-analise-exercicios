from math import pi
from math import sqrt
from math import e
def calcula_gaussiana(x,mi,sigma):
    x1 = 1/(sigma*sqrt(2*pi))
    x2 = ((x-mi)/sigma)**2
    gauss = x1*e**(-0.5*(x2))
    return gauss
    
    