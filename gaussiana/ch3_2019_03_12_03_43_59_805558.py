from math import *
def calcula_gaussiana(a,b,c):
    A = (1/(c*(sqrt(2*pi))))
    B = exp(((-1)*(0.5))*(((a - b)/c)**2))
    C = (A*B)
    return C
