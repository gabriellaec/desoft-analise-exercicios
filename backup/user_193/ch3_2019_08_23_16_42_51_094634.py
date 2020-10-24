from math import pi
def calcula_gaussiana(x, m, s):
    f=(1/(s*(2*pi)**(1/2)))*((10)**((-0.5*((x-m)/(s))**2)))
    return f