import math

def calcula_gaussiana (x, m , s):
    return (1/s*((2*math.pi)**1/2))*math.e**((-0.5*((x-m)/s))**2)