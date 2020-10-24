import math
def calcula_gaussiana(x,m,s):
    p1=(1/(((2*math.pi*(s**2))**(1/2))))
    p2=(math.exp((-0.5)*((x-m/s)**2)))
    return p1*p2
