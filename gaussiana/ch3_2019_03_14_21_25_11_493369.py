import math
def calcula_gaussiana(x,mi,sigma):
    y=(1/(sigma*math.sqrt(2*math.pi)))*math.exp(-0,5*((x-mi)/sigma)**2)
    return y
print (calcula_gaussiana(x,mi,sigma))