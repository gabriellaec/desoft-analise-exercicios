import math
def calcula_gaussiana(x,sigma,mi):
    y=((2*math.pi)**(1/2))*math.exp**(-0.5*((x-mi)/sigma)**2)/(sigma*2*math.pi)
    return y