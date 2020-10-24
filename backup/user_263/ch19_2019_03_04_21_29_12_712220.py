import math
def calcula_distancia_do_projetil(v,teta,Yo):
    g=9.8
    d= v**2/(2*g)*(1+(1+(2*g*Yo)/(v**2*(math.sin(teta))**2))**(1/2))
    return d