import math
def calcula_gaussiana(a,b,c):
    parte1 = 1/(c*((2*math.pi)**(1/2))
    parte2 = math.exp(-0.5*(((a-b)/c)**2))
    return parte1*parte2