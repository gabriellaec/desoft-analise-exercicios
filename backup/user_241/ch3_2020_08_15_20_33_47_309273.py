import math 
def calcula_gaussiana(x,u,si):
    return (1/(si * (2 * math.pi)**(1/2))) * math.exp(-0.5 * ((x - u)/si)**2)