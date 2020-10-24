import math
def calcula_distancia_do_projetil(v,y,o):
    parte1 = (v**2)/(2*9.8)
    parte2 = 1 + (1+ ((2*9.8*y)/(v**2*(math.sin(o))**2))**(1/2))
    parte3 = math.sin(2*o)
    return parte1*parte2*parte3