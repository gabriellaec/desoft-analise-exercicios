from math import pi, e

x = 1
mi = 1
sigma = 1

def calcula_gaussiana (x, mi, sigma):
    y = 1/(sigma*((2*pi)**(1/2)))*e**(-0.5*(((x - mi)/sigma)**2))
    return y

print (calcula_gaussiana(x, mi, sigma))