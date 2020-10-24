from math import *

def calcula_gaussiana(x, μ, σ):
    r = (e**(-0.5*((x-μ)/σ)**2))/σ*((2*pi)**(0.5))
    print(r) 
    
