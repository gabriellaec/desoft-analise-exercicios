import math

def calcula_gaussiana (x, mi, sig):
    parte1 = 1/(sig*(2*math.pi)**(1/2))
    parte2 = math.exp(-0.5((x-mi)/sig)**2)
    final = parte1 * parte2 
    
    return final