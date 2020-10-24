import math

def calcula_gaussiana(x,mi,sigma):
    
    return (1/(sigma*(2*math.pi)**0.5))*math.exp((-0.5*((x-mi)/sigma)**2))