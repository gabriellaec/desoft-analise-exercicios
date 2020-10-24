import math

def calcula_gaussiana (a, b, c):
    gaussiana = (1/(b*(2*math.pi)**1/2))*(math.e)**(-0.5((a-c)/b)**2)
    return(gaussiana)