import math

def calcula_distancia_do_projetil(v, th, h):
    
    sinth = math.sin(math.radians(th))
    
    if  sinth == 0.0:
        return -1
    
    if (th + 90) % 180 == 0 or v == 0:
        return 0
    
    preparte = 1 + ((19.6 * h) / ((v * sinth)**2))
    
    if preparte < 0.0:
        return 0
    
    parte1 = v**2 / 19.6

    parte2 = 1.0 + math.sqrt(preparte)

    parte3 = math.sin(math.radians(2*th))

   

    return parte1 * parte2 * parte3