import math
def calcula_gaussiana(x,u,o):
    return((math.e**(-0.5*((x-u)/o)**2))/o*sqrt(2*pi))