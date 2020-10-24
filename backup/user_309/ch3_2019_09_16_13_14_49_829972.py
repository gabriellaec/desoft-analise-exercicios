from math import e, sqrt, pi

def calcula_gaussiana(x,mi,sigma):
    gauss = 1/(sigma*sqrt(2*pi))*e**(-0,5*float(x-mi/sigma)**2)
    return gauss