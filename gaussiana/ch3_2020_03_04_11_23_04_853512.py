import math

def calcula_gaussiana(x, mi, sigma):
    a = 1/(sigma*math.sqrt(2*math.pi))
    b = math.e**(((x - mi)/sigma)**2*(-0.5))
    c = a*b
    return c

calcula_gaussiana(0, 0, 1)
calcula_gaussiana(2, 2, 1)
calcula_gaussiana(1000000000, -1000000000, 0.1)
calcula_gaussiana(2, 2, 1/(2*math.pi)**(0.5))
calcula_gaussiana(0, 1/math.sqrt(2*math.pi), 1/math.sqrt(2*math.pi))
calcula_gaussiana(1/(math.sqrt(2*math.pi)), 0, 1/math.sqrt(2*math.pi))