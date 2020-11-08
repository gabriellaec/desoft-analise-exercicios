import math 
import exp
def calcula_gaussiana(x,mi,sigma):
    d1=1/sigma*(2*math.pi)**1/2
    d2=(math.exp)**(-0.5*(x-mi)**2/sigma**2)
    d=d1*d2
    return d