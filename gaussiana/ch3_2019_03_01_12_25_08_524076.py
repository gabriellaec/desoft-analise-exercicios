import math.pi
def calcula_gaussiana(x,y,z):
    g=1/(z*2*pi**(1/2))**(0.5*((x-y)/z)**2)
    return g
