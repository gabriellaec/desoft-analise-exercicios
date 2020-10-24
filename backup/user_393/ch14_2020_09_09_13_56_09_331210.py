import math
def calcula_distancia_do_projetil(v,T,y):
    w= (v**2/(2*9.8))
    k= (1+(1+(2*9.8*y)/(v**2)*(math.sin(T))**2)**(1/2))
    f= (math.sin(2*T))
    x= w*k*f
    return x