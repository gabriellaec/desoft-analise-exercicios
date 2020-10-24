import math
def calcula_gaussiana(x,m,s):
    y=((math.e)**(-0.5*((x-m)/s)**2))/(s*(2*(math.pi))**0.5)
    return y