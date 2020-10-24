import math
def calcula_distancia_do_projetil (v, a, y0):
    p1= v**2/(2*9.8) 
    p2= 1+(1+ 2*9.8*y0/v**2 * (math.sin(a))**2)**0.5
    p3= math.sin(2*a)
    d=p1*p2*p3
    return d