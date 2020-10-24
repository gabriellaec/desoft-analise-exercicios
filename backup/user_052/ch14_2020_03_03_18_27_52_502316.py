import math 

def calcula_distancia_do_projetil (v,o,yo):
    a=(v**2/ (2 * 9.8))
    b=(1 + math.sqrt (1 + (2 * 9.8 * yo )/ (v**2 * (math.sin (o))**2))
    c= math.sin(2*o)
    return (a*b*c)