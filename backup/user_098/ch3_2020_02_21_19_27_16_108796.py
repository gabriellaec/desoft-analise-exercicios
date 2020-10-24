import math

def calcula_gaussiana(a,b,c):
    k = 1/(a*((2*math.pi)**(1/2)))*math.exp((-1/2)*((a-b)/c)**2)
    return k