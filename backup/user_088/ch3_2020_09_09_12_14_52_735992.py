import math 
e=2.7
def calcula_gaussiana(x,mi,sigma):
    gauss= e**(-0.5*((x-mi)/sigma))**2/sigma*((2*math.pi)**(1/2))
    return gauss