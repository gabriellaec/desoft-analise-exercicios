import math
def calcula_gaussiana(x,m,s):
    y = (1/s*math.sqrt(2*math.pi))*(math.e**(-0.5*((x-m)/s)**2))
    return y