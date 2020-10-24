import math
def calcula_gaussiana(x,mi,sigma):
    y=math.e**(-0.5*((x-mi)/sigma)**2)/(sigma*(2*math.pi)**1/2)
    return y
print (calcula_gaussiana(x,mi,sigma))
