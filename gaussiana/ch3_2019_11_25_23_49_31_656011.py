import math
def calcula_gaussiana(x,mi,sigma):
    y = (1/(sigma*((math.pi*2)**0.5)))*(math.e**(-0.5*((x-mi)/sigma)*2))
    return y