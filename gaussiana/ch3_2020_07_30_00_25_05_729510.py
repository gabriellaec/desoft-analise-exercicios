import math 
def calcula_gaussiana(x,u,si):
    y = [1/si*((2*math.pi)**1/2)]**[(-0.5)*((x-u)/si)**2]
    return y