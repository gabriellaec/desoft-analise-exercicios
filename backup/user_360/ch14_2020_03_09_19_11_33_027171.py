import math

def calcula_distancia_do_projetil(v,teta,y0):
    a= (v**2)/(2*9.8) 
    b= 2*9.8*y0
    c= v**2*(math.sin(2*teta)**2)
    d= math.sqrt(1+ (b/c))
    e= a*(1+d) * math.sin(2*teta)
    return e
