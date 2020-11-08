import math
def calcula_gaussiana(x,m,s):
    a=1/(s*math.sqrt(2*math.pi))
    b= math.e**(-0.5*((x-m)/s)**2)
    return(a*b)