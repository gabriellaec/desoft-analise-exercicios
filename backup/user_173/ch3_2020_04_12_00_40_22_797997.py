from math import *

def calcula_gaussiana (x,mi,sigma):
    f = 1/sigma*((2*pi)**0.5)*exp**(-0.5*((x-mi)/sigma)*2)
    return f                               