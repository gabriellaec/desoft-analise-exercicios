import math 
def calcula_distancia_do_projetil(v,y0,teta):
    
    d= ((v**2)/(2*9.8)) * (1+((1+((2*9.8*y0)/(v**2((math.sin(teta))**2))**0.5))))*math.sin(2*(teta))
    return d
g=9.8