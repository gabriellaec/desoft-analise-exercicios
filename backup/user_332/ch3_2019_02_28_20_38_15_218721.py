import math

def calcula_gaussiana (x, sigma, mi):
    gaussiana = (1/(sigma*(2*math.pi)**(1/2)))*(math.e)**(-0.5*((x-mi)/sigma)**2)
    return(gaussiana)