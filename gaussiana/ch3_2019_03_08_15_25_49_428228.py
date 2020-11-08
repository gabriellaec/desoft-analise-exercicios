import math

def calcula_gaussiana(x,mi,sigma):
    y=(1/sigma*(2*math.pi)**1/2)**(-0.5*((x-mi)/sigma)**2)
    if sigma==0:
        return ("Erro")
 
    return y
	