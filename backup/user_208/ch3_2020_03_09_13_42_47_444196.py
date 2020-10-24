import math

def calcula_gaussiana (x,mi,sigma):
    calculo = (1/(sigma*(2*math.pi)**(1/2)))*math.e**(-0,5*((x-mi)/sigma)**2)
    return calculo
x=5
mi=5
sigma=5
calculo=calcula_gaussiana (x,mi,sigma) 
print (calculo)