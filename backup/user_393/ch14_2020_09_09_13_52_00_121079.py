import math
def calcula_distancia_do_projetil(v,t,y):
    w= v**2/(2*9.8)
    k= 1+(1+(2*9.8*y)/(v**2)*(math.sin(t))**2)**(1/2)
    f= math.sin(2*t)
    x= w*k*f
    return x