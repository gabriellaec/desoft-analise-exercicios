import math
def calcula_distancia_do_projetil(v,alpha,y0):
    g = 9.8
    d = ((v**2)/2*g)*(1 + ( 1 + ( (2*g*y0)/v**2*(math.sin(alpha))**2)**(0.5))*math.sin(2*alpha)
    return d
    