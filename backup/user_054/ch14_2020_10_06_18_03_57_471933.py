import math
g= 9.8

def calcula_distancia_do_projetil (v, t, y0):
    return (v**2)/(2*g)*(1+(1+(2*g*y0)/(math.sin(t))**2*v**2)**(1/2))*math.sin(2*t)
                       
                       