from math import *
def calcula_gaussiana(x, mi, sigma):
    A = (1/(sigma*(sqrt(2*pi))))
    B = ((exp((-1)*(1/2)*(((x - mi)/sigma)**2))))
    valor_gaussiana =  A*B
    return valor_gaussiana