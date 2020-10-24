import math

def calcula_distancia_do_projetil(v,y0,teta):
    p1= (v**2)/(2*98/10) * (math.sin(2*teta))
    p2= (1+ 1+(2*9.8*y0/v**2*(math.sin(teta**2))**1/2)
    return p1*p2