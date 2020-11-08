import math
def calcula_gaussiana(x,m,s):
    y=(1/s*(2*math.pi)**(1/2))**(-0.5*((x-m)/s)**2)
    return y