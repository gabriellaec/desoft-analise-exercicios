import math
def calcula_gaussiana(x,mi,sigma):
    if x,mi,sigma!=0,0,0:
        f=(1/(sigma*math.sqrt(2*math.pi)))*math.exp((-1)*(1/2)*((x-mi)/sigma)**2)
        return f