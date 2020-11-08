from math import *

def calcula_gaussiana(x, μ, σ):
    r = (e**(-1/2*((x-μ)/σ)**2))/σ*((2*pi)**(1/2))
    return r 
