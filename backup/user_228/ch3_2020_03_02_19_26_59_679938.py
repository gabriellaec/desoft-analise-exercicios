import math
def calcula_gaussiana(x,m,s):
    a=1/(s*(2*math.pi)**1/2)
    b= math.e**(-0.5*((x-m)/s)**2)
    return(a*b)


    
    