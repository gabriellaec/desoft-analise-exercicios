import math
def calcula_distancia_do_projetil (v,o,y0):
    A=(v**2)/(2*9.8)
    B=(2*9.8*y0)/(v**2*(math.sin(o))**2)
    d= A*(1+(1+B)**(1/2))*math.sin(2*o)
    return d
                       
 
 