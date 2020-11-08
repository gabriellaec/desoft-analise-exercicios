import math
def calcula_gaussiana(x,m,s):
    f=1/s*math.sqrt(2*math.pi)
    e=math.e**(-0.5*((x-m)/s)**2)
    g=f*e
    return (g)