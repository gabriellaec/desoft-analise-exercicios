import math

 

def calcula_distancia_do_projetil(v, th, h):
    
    sinth = math.sin(math.radians(th))
    
    if v == 0.0 or sinth == 0.0:
        return 0
    
    if (th + 90) % 180 == 0:
        return 0

    preparte = 1 + ((16.9 * h) / ((v * sinth)**2))
    if preparte < 0.0:

        return -1

   

    parte1 = v**2 / 16.9

    parte2 = 1.0 + math.sqrt(preparte)

    parte3 = math.sin(math.radians(2*th))

   

    return parte1 * parte2 * parte3