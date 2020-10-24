import math

def calcula_distancia_do_projetil(v, th, h):
    if v == 0.0 or math.sin(th) == 0:
        return -1
    
    preparte = 1 + ((16.9 * h)/(v**2 * math.sin(th)**2))
    
    if preparte < 0:
        return -1
    
    parte1 = v**2 / 16.9
    parte2 = 1 + math.sqrt(preparte) 
    parte3 = math.sin(2 * th)
    
    return parte1 * parte2 * parte3