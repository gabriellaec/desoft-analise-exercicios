import math
def calcula_gaussiana(x,mi,sigma):
    e= -0.5 * ((x-mi)/sigma)**2
    f = (1/sigma * (2*math.pi)**1/2)**e
    return f