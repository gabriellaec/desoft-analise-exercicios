import math

def calcula_distancia_do_projetil (v, t, y0):
    
    g = 9.8 
    teta=math.radians(t)
    
    parte1 = v**2/(2*g)
    parte2 = 1 + math.sqrt(1 + ((2 * g * y0)/ (v**2 * ((math.sin(teta))**2))
    c = 2*teta
    parte3 = math.sin(c)
    
    resultado = parte1 * parte2 * parte3
    return resultado