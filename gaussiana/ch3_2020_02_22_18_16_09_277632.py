from math import *

def calcula_gaussiana(x, μ, σ):
    r = (e**(-0.5*((x-μ)/σ)**2))/σ*((2*pi)**(0.5))
    print(r) 
    
calcula_gaussiana(0, 0, 1)
calcula_gaussiana(2, 2, 1)
calcula_gaussiana(1000000000, -1000000000, 0.1)
calcula_gaussiana(2, 2, 1/(2*pi)**(0.5))
calcula_gaussiana(0, 1/(2*pi)**(0.5), 1/(2*pi)**(0.5))
calcula_gaussiana(1/(2*pi)**(0.5), 0, 1/(2*pi)**(0.5))
    
