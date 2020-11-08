import math
def calcula_gaussiana(x,mi,sigma):
    y=(1/sigma*(math.sqrt(2*math.pi)))*math.exp**((-1/2)*((x-mi)/sigma)**2)
    return y