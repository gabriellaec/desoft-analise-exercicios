import math 
def calcula_distancia_do_projetil(v,y0,g,teta):
    g=9.8
    d= ((v**2)/(2*g)) * (1+((1+((2*g*y0)/(v**2((math.sin(teta))**2))**0.5))))*math.sin(2*(teta))
    return d