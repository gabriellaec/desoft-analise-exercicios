import math
def calcula_gaussiana(x,mi,sigma):
    expo=(-0.5)*((x-mi)/sigma)**2
    f=(1/(sigma*math.sqrt(2*math.pi)))*math.exp(expo)
    return f
