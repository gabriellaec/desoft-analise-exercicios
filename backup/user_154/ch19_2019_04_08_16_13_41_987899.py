import math

def calcula_distancia_do_projetil(v, th, h):
    g = 9.8
    
    if v == 0 or (th + 90) % 180 == 0:
        return 0
    
    if th % 180 == 0:
        return math.sqrt(2 * h / g) * v
    
    preparte = 1.0 + ((2 * g * h) / ((v * math.sin(th))**2))

    if preparte < 0.0:
        return -1
    
    parte1 = v**2 / (2 * g)
    parte2 = math.sin(2*th)
    parte3 = math.sqrt(preparte)
    
    
    return parte1 * parte2 * parte3