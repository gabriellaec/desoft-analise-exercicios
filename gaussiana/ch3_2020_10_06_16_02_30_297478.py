import math

def calcula_gaussiana (x, m , o):
    return (1/o*((2*math.pi)**1/2))*math.e**((-0.5((x-m)/o))**2)