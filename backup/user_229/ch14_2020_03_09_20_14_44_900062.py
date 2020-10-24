import math
g=9.8
def calcula_distancia_do_projetil(v,g,yo,T):
    d=(v**2/2*g)*(1+(1+2*g*yo/v**2*(math.sin(T))**2)**(1/2))*(math.sin(T))
    return d