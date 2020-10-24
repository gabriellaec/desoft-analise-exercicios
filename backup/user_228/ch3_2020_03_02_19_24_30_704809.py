import math
def calcula_gaussiana(x,m,s):
    P1=1/s*(2*math.pi)**1/2
    P2=math.e**(-0.5*(x-m/s)**2)
    return (P1*P2)


    
    