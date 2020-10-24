import math 
import e
def calcula_gaussiana(x,mi,sigma):
    calcula_gaussiana= e**(-0.5*((x-mi)/sigma))**2)/sigma*((2*math.pi)**(1/2))
    return calcula_gaussiana