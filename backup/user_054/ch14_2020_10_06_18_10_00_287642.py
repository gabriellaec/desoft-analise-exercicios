import math
g= 9.8

def calcula_distancia_do_projetil (v, t, y0):
    pt_1 = (v**2)/(2*g)
    pt_2 = 1 + (1 + ((2*g*y0)/v**2*(math.sin(t))**2)**(1/2)
    pt_3 = math.sin(2*t)
    return pt_1*pt_2*pt_3                      
                       