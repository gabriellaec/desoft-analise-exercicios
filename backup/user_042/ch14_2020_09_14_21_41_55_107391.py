import math
def calcula_distancia_do_projetil(v,T,h):
    d= ((v**2)/(2*9.8))
    f= (1+(1+ (2*9.8*h)/(v**2 *(math.sin(T))**2))**(1/2))
    e= (math.sin(2*T))
    
    x=d*f*e
    return x