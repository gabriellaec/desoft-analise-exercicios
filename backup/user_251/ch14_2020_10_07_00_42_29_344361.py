import math
def calcula_distancia_do_projetil(v,o,y):
    d = (v**2)/(2*9.8)*(1 + (math.sqrt(1 + (2*9.8*y)/(v**2)*(math.sin(math.radians(o))**2)))*math.sin(math.radians(2*o)))
    return d 
    

