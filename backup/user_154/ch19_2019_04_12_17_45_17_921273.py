import math

def calcula_distancia_do_projetil(v, th, h):
    g = 9.8
    
    preparte = 2*g*h / (v**2 * (math.sin(th))**2)
    
    parte = math.sqrt(1 + preparte)
    
    return v**2/(2*g) * (1 + parte) * math.sin(2*th)