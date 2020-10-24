import math

def calcula_gaussiana (x, mi, si):
    chato = math.sqrt(2*math.pi)
    parte1 = 1/(si * chato)
    parte2 = math.exp(-0.5*((x-mi)/si)**2)
    
    funcao = parte1*parte2
    
    return funcao