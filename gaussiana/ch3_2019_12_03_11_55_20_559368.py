from math import e
from math import pi
def calcula_gaussiana(x,y,z):
    F = (1/z*(2*pi)**1/2)*e**(-0.5*((x-y)/z)**2)
    return F