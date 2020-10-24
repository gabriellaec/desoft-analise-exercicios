import math

def calcula_distancia_do_projetil(v, th, h):
    g = 9.8
    
    preparte = 1.0 + ((2 * g * h) / ((v * math.sin(th))**2))
    
    parte1 = v**2 / (2 * g)
    parte2 = math.sin(2*th)
    parte3 = math.sqrt(preparte)
    
    return parte1 * (1 + parte2) * parte3