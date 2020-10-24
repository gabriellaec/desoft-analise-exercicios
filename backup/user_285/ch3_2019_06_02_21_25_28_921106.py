from math import e, sqrt, pi
def calcula_gaussiana(x, mu, sig):
    gauss = 1/(sqrt(2*pi)*sig)*e**(-0.5*((x-mu)/sig)**2)
    return gauss
a=1
b=0
c=2
t= calcula_gaussiana(a,b,c)
