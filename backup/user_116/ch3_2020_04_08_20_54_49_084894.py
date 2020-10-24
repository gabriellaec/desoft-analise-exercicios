import math
def calcula_gaussiana(x,m,s):
    p1=(1/(s*(2*math.pi)**(1/2)))
    p2=math.exp((-0.5)*(x-m/s)**2)
    return p1*p2
