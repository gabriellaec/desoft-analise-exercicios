from math import e, sqrt, pi

def calcula_gaussiana (x, mi, sigma):
    y = 1/(sqrt(2*pi)*sigma)*e**(-0.5*(x-mi/sigma)**2)
    return y
a= 1
b= 2
c= 30

gauss = calcula_gaussiana(a,b,c)
print (gauss)