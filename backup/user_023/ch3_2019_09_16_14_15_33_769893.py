import math
def calcula_gaussiana(x,m,s):
    A= math.e**(-0.5*((x-m)/s)**2)
    B= s*(2*math.pi)**(1/2)
    f = 1/B*A
    return f