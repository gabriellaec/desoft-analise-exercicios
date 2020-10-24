import math
def calcula_distancia_do_projetil(v,o,y):
    o_ = math.radians(o)
    parte1 = (v**2)/(2*9.8)
    parte2 = 1 + ( 1+ (2*9.8*y)/(v**2)*((math.sin(o_)))**2)**(1/2)
    parte3 = math.sin(2*o_)
    return parte1*parte2*parte3