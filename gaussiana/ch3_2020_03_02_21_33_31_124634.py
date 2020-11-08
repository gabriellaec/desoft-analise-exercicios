from math import *

def calcula_gaussiana(x, μ, σ):
    a = 1/(σ*sqrt(2*pi))
    b = e**((x - μ/σ)**2*(-0.5))
    c = a*b
    return c

calcula_gaussiana(0, 0, 1)
calcula_gaussiana(2, 2, 1)
calcula_gaussiana(1000000000, -1000000000, 0.1)
calcula_gaussiana(2, 2, 1/(2*pi)**(0.5))
calcula_gaussiana(0, 1/(2*pi)**(0.5), 1/(2*pi)**(0.5))
calcula_gaussiana(1/(2*pi)**(0.5), 0, 1/(2*pi)**(0.5))
