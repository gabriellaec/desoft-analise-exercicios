import math as m 
def calcula_gaussiana(x,mi,omeg):
    p1 = omeg*m.sqrt(2*m.pi)
    p2 = -0.5*(((x-mi)/omeg)**2)
    return m.exp(p2)/p1
