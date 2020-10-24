import math
def calcula_distancia_do_projetil (v,o,y0):
    parte1 = v**2/2*9.8
    parte2 = (1 + (1 + (2*9.8*y0)/(v**2*(math.sin(o))**2))**0.5)
    parte3 = math.sin(2*o)
    return (parte1*parte2*parte3)