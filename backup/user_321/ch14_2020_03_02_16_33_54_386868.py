import math
def calcula_distancia_do_projetil (v,o,y):
    return (v**2/(2*9.8))*(1+math.sqrt(1+(2*9.8*y)/(v**2))*(math.sin(o))**2)*math.sin(2*o)