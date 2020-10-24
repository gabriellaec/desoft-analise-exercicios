import math

def calcula_gaussiana (x, mi, si):
    parte1 = 1/(si * (math.sqrt(2*math.pi)))
    parte2 = math.exp(-0.5*((x-mi)/si)**2)
    
    funcao = parte1/parte2
    
    return funcao