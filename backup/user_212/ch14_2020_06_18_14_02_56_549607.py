import math

def calcula_distancia_do_projetil (v, t, y0):
    
    g = 9.8 
    
    parte1 = v**2/(2*g)
    parte2 = 1 + math.sqrt(1 + ((2 * g * y0)/ (v**2 * ((math.sin(t))**2))))
    c = 2*t
    parte3 = math.sin(c)
    
    resultado = parte1 * parte2 * parte3
    return resultado