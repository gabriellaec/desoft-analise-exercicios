import math as m 
def calcula_gaussiana(x,mi,omeg):
    p1 = omeg*sqrt(2*m.pi)
    p2 = -0.5*(((x-mi)/omega)**2)
    return m.exp(p2)/p1
