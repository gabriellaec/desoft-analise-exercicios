import math
def calcula_gaussiana(x,m,s):
    f=1/s*math.sqrt(2*math.pi)
    p=(math.e)**((-0.5)*((x-m)/s)**2)
    g=f*p
    return (g)