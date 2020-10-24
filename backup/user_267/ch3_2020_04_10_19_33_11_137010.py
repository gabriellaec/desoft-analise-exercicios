import math
def calcula_gaussiana(x, mi, sigma):
    a = sigma*((2*math.pi)**(1/2))
    b = -0.5*((x-mi)/sigma)**2
    gaussiana = ((1/a)*(math.e**b))
    return gaussiana