import math

def calcula_gaussiana (x,u,o):
    f= (1/o*((2*math.pi)**1/2))*math.exp(-0.5*((x-u/o)**2))
    return f