from math import exp, sqrt, pi
def calcula_gaussiana(x,y,z):
    return (1/(z*sqrt(2*pi)))*exp(-(0.5)*((x-y)/z)**2)