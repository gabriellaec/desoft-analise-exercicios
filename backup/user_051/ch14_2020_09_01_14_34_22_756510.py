import math as mt
def calcula_distancia_do_projetil(v, o, y):
    d=((v**2)/(2*9.8))*(1+mt.sqrt(1+(2*9.8*y)/(v**2*(mt.sin(o)**2))))*mt.sin(2*o)
    return d