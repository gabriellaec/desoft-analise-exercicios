import math
def calcula_gaussiana(x,a,b):
    y = 1/(b*(2*math.pi)**(1/2))*math.exp(-0,5*((x-a)/b)**2)
    return y