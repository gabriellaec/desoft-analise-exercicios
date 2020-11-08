import math
def calcula_gaussiana(x, mi, sigma):
    a=1/sigma*(2(math.pi)**1/2)
    b=2,71**(-0.5*((x-mi)/sigma)**2)
    c=a*b
    return c


