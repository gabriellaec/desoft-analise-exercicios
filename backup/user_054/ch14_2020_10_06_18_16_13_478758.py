import math
g= 9.8

def calcula_distancia_do_projetil (v, t, y0):
    return (v**2)/(2*g)*(math.sin(2*t))*(1 + ((1 + ((2*g*y0)/v**2*(math.sin(t))**2))**(1/2)))
                  
                       