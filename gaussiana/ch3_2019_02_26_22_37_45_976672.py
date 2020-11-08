import math
def calcula_gaussiana(x,mi,sigma):
    q1=1/(sigma*(2*math.pi)**0.5)
    q2=math.exp(-0.5*((x-mi)/sigma)**2)
    f=q1*q2
    return f