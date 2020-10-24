import math 

def calcula_gaussiana(x, mi, sigma): 
        return (1/(sigma*(2*math.pi)**(1/2)))**(-1/2*(x-mi/sigma)**2)

