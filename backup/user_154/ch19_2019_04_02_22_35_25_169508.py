import math

def calcula_distancia_do_projetil(v, th, h):
    g = 9.8
    
    if v == 0 or (th + 90) % 180 == 0:
        return 0
    
    if th % 180 == 0:
        return math.sqrt(2 * h / g) * v

    sinth = math.sin(math.radians(th))
    preparte = 1.0 + ((2 * g * h) / ((v * sinth)**2))

    if preparte < 0.0:
        return -1
    
    parte1 = v**2 / (2 * g)
    parte2 = 1.0 + math.sqrt(preparte)
    parte3 = math.sin(math.radians(2*th))
    
    return parte1 * parte2 * parte3