from math import *
x = float(input()) a 
mi = float(input()) b
sigma = float(input()) c
def calcula_gaussiana(a,b,c):
    A = (1/(c*(sqrt(2*pi))))
    B = ((-1)*(0.5))*(((a - b)/c)**2)
    C = (exp(B))
    D = (A*C)
    return D
