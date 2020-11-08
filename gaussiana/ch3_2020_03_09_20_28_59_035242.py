import math
def calcula_gaussiana(x,mi,sigma):
    a=1/(sigma)*(2*math.pi)**0.5
    b=(math.e)**(-0.5)*((x-mi)/2)**2
    f=a*b
    return f