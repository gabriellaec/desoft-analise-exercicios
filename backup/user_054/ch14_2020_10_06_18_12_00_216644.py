import math
g= 9.8

def calcula_distancia_do_projetil (v, t, y0):
    a = (v**2)/(2*g)*math.sin(2*t)
    b = 1 + (1 + ((2*g*y0)/v**2*(math.sin(t))**2)**(1/2)
    return a*b                      
                       